from numpy import array, sqrt, sin, cos, deg2rad, rad2deg, arctan, pi, hstack, vstack, zeros, dot, linalg
from tabulate import tabulate

def computeRotationMatrix(geoRefPoint):
    """
    compute the needed rotation matrix given a geographic reference point
    :param geoRefPoint: the ref point tuple
    :return: rotation matrix
    """
    R = array([[cos(geoRefPoint[0]) * cos(geoRefPoint[1]), cos(geoRefPoint[0]) * sin(geoRefPoint[1]),
                sin(geoRefPoint[0])]
                  , [-sin(geoRefPoint[1]), cos(geoRefPoint[1]), 0]
                  , [-sin(geoRefPoint[0]) * cos(geoRefPoint[1]), -sin(geoRefPoint[0] * sin(geoRefPoint[1])),
                     cos(geoRefPoint[0])]])
    return R


def computeDesignMatrix(data):
    """

    :param data:
    :return:
    """
    A = zeros((data.shape[0], 4))
    for i, sat in enumerate(data):
        roh = sqrt(sat[1] ** 2 + sat[2] ** 2 + sat[3] ** 2)
        A[i, :] = [-sat[1] / roh, -sat[2] / roh, -sat[3] / roh, -1]

    return A


# station and time data
bshm = array([deg2rad(32 + 46 / 60 + 44.34472 / 3600), deg2rad(35 + 1 / 60 + 22.74061 / 3600), 225.046])
crit_angle = 15  # deg
begin_time = array([6, 0])
end_time = array([7, 0])

# WGS84 data
a = 6378137  # m
f = 1 / 298.257223563
e_squared = 2 * f - f ** 2
N = a / sqrt(1 - e_squared * (sin(bshm[0])) ** 2)

# base station u,v,w in m
bshm_uvw = array([(N + bshm[2]) * cos(bshm[0]) * cos(bshm[1]), (N + bshm[2]) * cos(bshm[0]) * sin(bshm[1]),
                  (N * (1 - e_squared) + bshm[2]) * sin(bshm[0])])

with open(r'C:\Users\Saul\PycharmProjects\GPS-Surveying\gfz20951.sp3') as file:
    lines = file.readlines()
    line0 = lines[0].split()
    date = [int(line0[2]), int(line0[1]), int(''.join(map(str, [int(i) for i in line0[0] if i.isdigit()])))]
    data = []  # storing only relevant data from SP3 file
    for i in range(22,len(lines)):
        try:
            line = lines[i].split()
            if int(line[1]) == date[2] and int(line[2]) == date[1] and int(line[3]) == date[0] and int(line[4]) == begin_time[0] and int(line[5]) == begin_time[1]:

                j = i
                end_line = lines[i].split()
                end_line = hstack(end_line[4:6]).astype(int)
                while end_line[0] != end_time[0] or end_time[1] != end_time[1]:
                    data.append(lines[j].split()[0:5])
                    j += 1
                    end_line = lines[j].split()
                    if len(end_line) >= 7:
                        end_line = hstack(end_line[4:6]).astype(int)
                break
        except:
            continue

data = vstack(data)

# calc rotation matrix:
P = computeRotationMatrix(bshm[0:2])

# compute GPS to Base station differences :
delta_data = data.copy()
uen_data = delta_data.copy()
for i, sat in enumerate(delta_data):
    if sat[0] == '*':
        sat[0] = 0
        uen_data[i, 0] = 0
    else:
        uen_data[i, 0] = uen_data[i, 0].replace('PG', '0')
        uen_data[i, 0] = uen_data[i, 0].replace('PR', '0')
        sat[0] = sat[0].replace('PG', '0')
        sat[0] = sat[0].replace('PR', '0')
        sat[1] = float(sat[1]) - bshm_uvw[0] / 1000
        sat[2] = float(sat[2]) - bshm_uvw[1] / 1000
        sat[3] = float(sat[3]) - bshm_uvw[2] / 1000

        # compute coordinates in (n,e,u)
        uen_data[i, 1:4] = dot(P, sat[1:4].astype(float).T)

delta_data = delta_data.astype(float)
uen_data = uen_data.astype(float)
# iterating again to compute beta angles of every satellite
visibleSats = []
sat_count = 0
for i, sat in enumerate(uen_data):
    if sat[0] == 0.:
        visibleSats.append(hstack((sat,0)))
    else:
        # computing beta angle of sat
        beta = rad2deg(arctan(sat[1] / (sqrt(sat[2] ** 2 + sat[3] ** 2))))
        if beta >= crit_angle:
            sat = hstack((sat, 0))
            sat[5] = beta
            visibleSats.append(hstack((delta_data[i, 0:5], beta)))

visibleSats = vstack(visibleSats)

sats_in_hours = []
chk_indices = []
design_mas = []

# checking indices where we should break the data
j = 0
for sat in visibleSats:
    if sat[0] == 0.:
        chk_indices.append(j)
    j += 1

chk_indices.pop(0)
sats_in_hours.append(visibleSats[1:chk_indices[0], :])
design_mas.append(computeDesignMatrix(visibleSats[1:chk_indices[0], :]))

# collecting data of satellites per time and computing design matrices
for i, num in enumerate(chk_indices):
    try:
        sat_chunk = visibleSats[num + 1:chk_indices[i + 1], :]
        sats_in_hours.append(sat_chunk)
        design_mas.append(computeDesignMatrix(sat_chunk))
    except:
        leng = len(visibleSats)
        sat_chunk = visibleSats[num + 1:leng, :]
        sats_in_hours.append(sat_chunk)
        design_mas.append(computeDesignMatrix(sat_chunk))

# now for every design matrix we will compute the co-factor Qx
Qx = []
for a in design_mas:
    Qx.append(linalg.inv(dot(a.T, a)))

# computing the rest of the data needed
occ_data = []
for qx in Qx:
    q_uen = dot(dot(P, qx[0:3, 0:3]), P.T)
    occ_data.append(array(
        [sqrt(qx[0, 0] + qx[1, 1] + qx[2, 2] + qx[3, 3]), sqrt(qx[0, 0] + qx[1, 1] + qx[2, 2]), sqrt(qx[3, 3]),
         sqrt(q_uen[0, 0] + q_uen[1, 1] + q_uen[2, 2]), sqrt(q_uen[1, 1] + q_uen[2, 2]), sqrt(q_uen[0, 0])]))

# organizing data and printing :)
headers = ['Time', 'SV', 'Pdop', 'Hdop', 'Vdop', 'Tdop', 'Gdop']
results = []

# getting all the times
ti = begin_time.copy().tolist()
tf = end_time.copy().tolist()
time = []
time.append(ti)
while ti != tf:
    if ti[1] == 45:
        ti = [ti[0] + 1, 0]
        time.append(ti)
    else:
        ti = [ti[0], ti[1] + 15]
        time.append(ti)

# organizing data
for i, sat in enumerate(sats_in_hours):

    if time[i][1] == 0:
        res = array(['{}:{}0'.format(time[i][0], time[i][1]), sat.shape[0], '{:.2f}'.format(round(occ_data[i][1], 2)), '{:.2f}'.format(round(occ_data[i][4], 2)), '{:.2f}'.format(round(occ_data[i][5], 2)), '{:.2f}'.format(round(occ_data[i][2], 2)), '{:.2f}'.format(round(occ_data[i][0], 2))])
    else:
        res = array(['{}:{}'.format(time[i][0], time[i][1]), sat.shape[0], '{:.2f}'.format(round(occ_data[i][1], 2)), '{:.2f}'.format(round(occ_data[i][4], 2)), '{:.2f}'.format(round(occ_data[i][5], 2)), '{:.2f}'.format(round(occ_data[i][2], 2)), '{:.2f}'.format(round(occ_data[i][0], 2))])
    results.append(res)

results = vstack(results)

print(tabulate(results, headers, disable_numparse=True))


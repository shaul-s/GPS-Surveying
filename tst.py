from numpy import array, sqrt, sin, cos, deg2rad, rad2deg, arctan2

MainWindow.setFixedSize(1024, 720)


# additions
self.of_dialog.clicked.connect(self.openfile)
self.base_station.currentTextChanged.connect(self.basestation_comb)
self.begin_time.currentTextChanged.connect(self.time_selection)
self.end_time.currentTextChanged.connect(self.time_selection)
self.restart.clicked.connect(self.clear_all)
self.calc.clicked.connect(self.computeOccPlan)


def time_selection(self, value):
    pass


def basestation_comb(self, value):
    global base
    if value == '':
        self.latit.setText('')
        self.longit.setText('')
        self.height.setText('')

    if value == 'BSHM':
        self.latit.setText('''32°46'44.34472"''')
        self.longit.setText('''35°1'22.74061"''')
        self.height.setText('225.046')
        base = array([deg2rad(32 + 46 / 60 + 44.34472 / 3600), deg2rad(35 + 1 / 60 + 22.74061 / 3600), 225.046])

    if value == 'ELAT':
        self.latit.setText('''29°30'33.40506"''')
        self.longit.setText('''34°55'14.16064"''')
        self.height.setText('29.521')
        base = array([deg2rad(29 + 30 / 60 + 33.40506 / 3600), deg2rad(34 + 55 / 60 + 14.16064 / 3600), 29.521])


def openfile(self):
    global begin_time, end_time, data
    fname = QFileDialog.getOpenFileName(None, "Open data file", '.', "(*.sp3)")
    with open(fname[0], 'r') as file:
        lines = file.readlines()
        line0 = lines[0].split()
        self.lineEdit.setText(fname[0])
        self.num_sat.setText(lines[2].split()[1])
        date = [int(line0[2]), int(line0[1]), int(''.join(map(str, [int(i) for i in line0[0] if i.isdigit()])))]
        self.sp3date.setText("{} - {} - {}".format(int(date[0]), int(date[1]), int(date[2])))
        begin_time = hstack(self.begin_time.currentText().split(':')).astype(int).tolist()
        end_time = hstack(self.end_time.currentText().split(':')).astype(int).tolist()

        # gathering required data
        data = []  # storing only relevant data from SP3 file
        for i in range(len(lines)):
            line = lines[i]
            if line.rstrip('\n') == '*  {}  {} {} {} {}  0.00000000'.format(str(date[2]), str(date[1]),
                                                                            str(date[0]),
                                                                            str(begin_time[0]), str(begin_time[1])) \
                    or line.rstrip('\n') == '*  {}  {} {}  {}  {}  0.00000000'.format(str(date[2]), str(date[1]),
                                                                                      str(date[0]),
                                                                                      str(begin_time[0]),
                                                                                      str(begin_time[1])) \
                    or line.rstrip('\n') == '*  {}  {} {} {}  {}  0.00000000'.format(str(date[2]), str(date[1]),
                                                                                     str(date[0]),
                                                                                     str(begin_time[0]),
                                                                                     str(begin_time[1])) \
                    or line.rstrip('\n') == '*  {}  {} {}  {} {}  0.00000000'.format(str(date[2]), str(date[1]),
                                                                                     str(date[0]),
                                                                                     str(begin_time[0]),
                                                                                     str(begin_time[1])):

                j = i
                while lines[j].rstrip('\n') != '*  {}  {} {} {} {}  0.00000000'.format(str(date[2]), str(date[1]),
                                                                                       str(date[0]), str(end_time[0]),
                                                                                       str(end_time[1])) \
                        and lines[j].rstrip('\n') != '*  {}  {} {}  {}  {}  0.00000000'.format(str(date[2]),
                                                                                               str(date[1]),
                                                                                               str(date[0]),
                                                                                               str(end_time[0]),
                                                                                               str(end_time[1])) \
                        and lines[j].rstrip('\n') != '*  {}  {} {} {}  {}  0.00000000'.format(str(date[2]),
                                                                                              str(date[1]),
                                                                                              str(date[0]),
                                                                                              str(end_time[0]),
                                                                                              str(end_time[1])) \
                        and lines[j].rstrip('\n') != '*  {}  {} {}  {} {}  0.00000000'.format(str(date[2]),
                                                                                              str(date[1]),
                                                                                              str(date[0]),
                                                                                              str(end_time[0]),
                                                                                              str(end_time[1])):
                    data.append(lines[j].split()[0:6])
                    j += 1
                data = vstack(data)
                break


def clear_all(self):
    """

    :return:
    """
    self.num_sat.clear()
    self.lineEdit.clear()
    self.sp3date.clear()
    self.beta.clear()
    self.base_station.setCurrentIndex(0)
    self.begin_time.setCurrentIndex(0)
    self.end_time.setCurrentIndex(0)
    self.textBrowser.setText('')


def computeOccPlan(self):
    # WGS84 data
    a = 6378137  # m
    f = 1 / 298.257223563
    e_squared = 2 * f - f ** 2
    N = a / sqrt(1 - e_squared * (sin(base[0])) ** 2)

    # crit angle and time data
    crit_angle = float(self.beta.text())  # deg

    # base station u,v,w in m
    base_uvw = array([(N + base[2]) * cos(base[0]) * cos(base[1]), (N + base[2]) * cos(base[0]) * sin(base[1]),
                      (N * (1 - e_squared) + base[2]) * sin(base[0])])

    # calc rotation matrix:
    P = computeRotationMatrix(base[0:2])

    # compute GPS to Base station differences :
    delta_data = data.copy()
    uen_data = delta_data.copy()
    for i, sat in enumerate(delta_data):
        if sat[0] == '*':
            sat[0] = 0
            uen_data[i, 0] = 0
        else:
            uen_data[i, 0] = uen_data[i, 0].replace('PG', '0')
            sat[0] = sat[0].replace('PG', '0')
            sat[1] = float(sat[1]) - base_uvw[0] / 1000
            sat[2] = float(sat[2]) - base_uvw[1] / 1000
            sat[3] = float(sat[3]) - base_uvw[2] / 1000

            # compute coordinates in (n,e,u)
            uen_data[i, 1:4] = dot(P, sat[1:4].astype(float).T)

    delta_data = delta_data.astype(float)
    uen_data = uen_data.astype(float)

    # iterating again to compute beta angles of every satellite
    visibleSats = []
    sat_count = 0
    for i, sat in enumerate(uen_data):
        if sat[0] == 0.:
            visibleSats.append(sat)
        else:
            # computing beta angle of sat
            beta = rad2deg(arctan(sat[1] / (sqrt(sat[2] ** 2 + sat[3] ** 2))))
            if beta >= crit_angle:
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
    ti = begin_time.copy()
    tf = end_time.copy()
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
            res = array(
                ['{}:{}0'.format(time[i][0], time[i][1]), sat.shape[0], '{:.2f}'.format(round(occ_data[i][1], 2)),
                 '{:.2f}'.format(round(occ_data[i][4], 2)), '{:.2f}'.format(round(occ_data[i][5], 2)),
                 '{:.2f}'.format(round(occ_data[i][2], 2)), '{:.2f}'.format(round(occ_data[i][0], 2))])
        else:
            res = array(
                ['{}:{}'.format(time[i][0], time[i][1]), sat.shape[0], '{:.2f}'.format(round(occ_data[i][1], 2)),
                 '{:.2f}'.format(round(occ_data[i][4], 2)), '{:.2f}'.format(round(occ_data[i][5], 2)),
                 '{:.2f}'.format(round(occ_data[i][2], 2)), '{:.2f}'.format(round(occ_data[i][0], 2))])
        results.append(res)

    results = vstack(results)

    self.textBrowser.setText(tabulate(results, headers, disable_numparse=True))

    # plotting

    plt.plot(1, 1)
    plt.show()



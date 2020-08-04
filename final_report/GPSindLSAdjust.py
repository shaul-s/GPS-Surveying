from azimuth import *
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.linalg import inv
from scipy.linalg import block_diag, solve

def rotation2neu(geoRefPoint):
    R = np.array([[-np.sin(geoRefPoint[0]) * np.cos(geoRefPoint[1]), -np.sin(geoRefPoint[1]),
                   np.cos(geoRefPoint[0]) * np.cos(geoRefPoint[1])]
                     , [-np.sin(geoRefPoint[0]) * np.sin(geoRefPoint[1]), np.cos(geoRefPoint[1]),
                        np.cos(geoRefPoint[0]) * np.sin(geoRefPoint[1])]
                     , [np.cos(geoRefPoint[0]), 0, np.sin(geoRefPoint[0])]])
    return R


if __name__ == '__main__':
    # known reference
    GPS2_GEOGRAPHICAL = np.radians(np.array([32 + 46 / 60 + 47.55736 / 3600, 35 + 1 / 60 + 18.28410 / 3600]))
    GPS2_GEOCENTRICAL = np.array([4395954.6949, 3080567.6853, 3433565.9063])

    # loading data
    with open('indVecAdjust.csv', 'r') as file:
        lines = file.readlines()
        data = []
        q_matrices = []
        for i, line in enumerate(lines):
            line = line.split(',')
            try:
                line[2] = float(line[2])
            except:
                continue
            q = np.array([[line[6], line[7], line[8]], [line[7], line[9], line[10]], [line[8], line[10], line[11]]])
            q_matrices.append(q)
            data.append(np.array([line[2], line[3], line[4]]))
    data = np.array(data).astype(float)
    sig_Lb_ind = block_diag(*q_matrices[0:10]).astype(float)
    sig_Lb_dep = block_diag(*q_matrices[10:None]).astype(float)

    # F matrix
    F = np.array([[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0],
                  [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0]])


    # Weight Matrix
    P_ind = 1e-6 * inv(sig_Lb_ind)
    P_dep = 1e-6 * inv(sig_Lb_dep)

    P = (2/7)*(P_ind + np.dot(np.dot(F.T, P_dep), F))

    # observation matrix
    lb = data.flatten()[0:30]
    l0 = np.zeros(lb.shape)
    # applying known valeus to l0
    l0[21:24] = -GPS2_GEOCENTRICAL
    l0[27:30] = -GPS2_GEOCENTRICAL
    L = lb - l0

    # Design Matrix
    A = np.array([[-1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1],
                  [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    # Solving LS adjustment
    N = np.dot(np.dot(A.T, P), A)
    u = np.dot(np.dot(A.T, P), L)

    X = solve(N, u)
    # Residuals vector
    V = np.dot(A, X) - L
    # A-Posterior Variance-Covariance
    sig_Apost = np.dot(np.dot(V.T, P), V) / (L.shape[0] - A.shape[1])
    sig_X = sig_Apost * inv(N)

    # Transforming to topocentric coordinates
    R = rotation2neu(GPS2_GEOGRAPHICAL)
    X_diff = X - np.resize(GPS2_GEOCENTRICAL, X.shape)
    R_block = np.kron(np.eye(6, dtype=int), R)

    X_topo = np.dot(R_block.T, X_diff)
    sig_X_topo = np.dot(np.dot(R_block.T, sig_X), R_block)

    # ellipses in topocentric system
    # Error Ellipses
    ellipses_topo = np.zeros((6, 3))
    j = 0
    for row in ellipses_topo:
        row[0] = 0.5 * (
                sig_X_topo[j, j] + sig_X_topo[j + 1, j + 1] + np.sqrt(
            (sig_X_topo[j, j] - sig_X_topo[j + 1, j + 1]) ** 2 + 4 * sig_X_topo[j, j + 1] ** 2))
        row[1] = 0.5 * (
                sig_X_topo[j, j] + sig_X_topo[j + 1, j + 1] - np.sqrt(
            (sig_X_topo[j, j] - sig_X_topo[j + 1, j + 1]) ** 2 + 4 * sig_X_topo[j, j + 1] ** 2))
        row[2] = np.rad2deg(0.5 * azimuth(sig_X_topo[j, j] - sig_X_topo[j + 1, j + 1], 2 * sig_X_topo[j, j + 1]))
        j += 3
    ellipses_topo[:, 0:2] = np.sqrt(ellipses_topo[:, 0:2])

    # exporting to csv
    # pd.DataFrame(P).to_csv('P_star.csv')
    # pd.DataFrame(L).to_csv('L_ind.csv')
    # pd.DataFrame(A).to_csv('A_ind.csv')
    # pd.DataFrame(np.reshape(X, (6, 3))).to_csv('X_ind.csv')
    # pd.DataFrame(V).to_csv('V_ind.csv')
    # pd.DataFrame(sig_X).to_csv('sig_X_ind.csv')
    # # pd.DataFrame(ellipses).to_csv('ellipses.csv')
    # pd.DataFrame(ellipses_topo).to_csv('ellipses_topo_ind.csv')
    # pd.DataFrame(np.reshape(X_topo, (6, 3))).to_csv('X_topo_ind.csv')
    # pd.DataFrame(F).to_csv('F.csv')


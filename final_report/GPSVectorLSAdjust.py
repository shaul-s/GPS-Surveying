from azimuth import *
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.linalg import inv
from scipy.linalg import block_diag, solve
from tabulate import tabulate



def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv += [r'\end{bmatrix}']
    return '\n'.join(rv)


def rotation2neu(geoRefPoint):
    R = np.array([[-np.sin(geoRefPoint[0]) * np.cos(geoRefPoint[1]), -np.sin(geoRefPoint[1]),
                   np.cos(geoRefPoint[0]) * np.cos(geoRefPoint[1])]
                     , [-np.sin(geoRefPoint[0]) * np.sin(geoRefPoint[1]), np.cos(geoRefPoint[1]),
                        np.cos(geoRefPoint[0]) * np.sin(geoRefPoint[1])]
                     , [np.cos(geoRefPoint[0]), 0, np.sin(geoRefPoint[0])]])
    return R


if __name__ == '__main__':
    with open('1ST_PROCESS_ALL_VECS.csv', 'r') as file:
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
        sig_Lb = block_diag(*q_matrices).astype(float)
        # Weight Matrix
        P = 1e-6 * inv(sig_Lb)

        GPS2_GEOGRAPHICAL = np.radians(np.array([32 + 46 / 60 + 47.55736 / 3600, 35 + 1 / 60 + 18.28410 / 3600]))
        GPS2_GEOCENTRICAL = np.array([4395954.6949, 3080567.6853, 3433565.9063])

        Lb = data.flatten()
        L0 = np.zeros(Lb.shape)
        L0[30:33] = + GPS2_GEOCENTRICAL
        L0[33:36] = - GPS2_GEOCENTRICAL
        L0[36:39] = + GPS2_GEOCENTRICAL
        L0[42:45] = - GPS2_GEOCENTRICAL

        # Observations Matrix
        L = Lb - L0
        # Design Matrix
        A = np.array([[-1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                      [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1],
                      [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                      [-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        # Solving LS adjustment
        N = np.dot(np.dot(A.T, P), A)
        u = np.dot(np.dot(A.T, P), L)

        X = solve(N, u)
        # Residuals vector
        V = np.dot(A, X) - L
        # A-Posterior Variance-Covariance
        sig_Apost = np.dot(np.dot(V.T, P), V) / (L.shape[0] - A.shape[1])
        sig_X = sig_Apost * inv(N)

        # Error Ellipses
        ellipses = np.zeros((6, 3))
        j = 0
        for row in ellipses:
            row[0] = 0.5 * (
                    sig_X[j, j] + sig_X[j + 1, j + 1] + np.sqrt(
                (sig_X[j, j] - sig_X[j + 1, j + 1]) ** 2 + 4 * sig_X[j, j + 1] ** 2))
            row[1] = 0.5 * (
                    sig_X[j, j] + sig_X[j + 1, j + 1] - np.sqrt(
                (sig_X[j, j] - sig_X[j + 1, j + 1]) ** 2 + 4 * sig_X[j, j + 1] ** 2))
            row[2] = np.rad2deg(0.5 * azimuth(sig_X[j, j] - sig_X[j + 1, j + 1], 2 * sig_X[j, j + 1]))
            j += 3
        ellipses[:, 0:2] = np.sqrt(ellipses[:, 0:2])

        # exporting to csv / spying
        # plt.spy(P, markersize=5)
        # plt.show()
        # pd.DataFrame(P).to_csv('P.csv')
        # pd.DataFrame(L).to_csv('L.csv')
        # pd.DataFrame(A).to_csv('A.csv')
        # pd.DataFrame(np.reshape(X, (6, 3))).to_csv('X.csv')
        # pd.DataFrame(V).to_csv('V.csv')
        # pd.DataFrame(sig_X).to_csv('sig_X.csv')
        # pd.DataFrame(ellipses).to_csv('ellipses.csv')



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

        # pd.DataFrame(ellipses_topo).to_csv('ellipses_topo.csv')
        # pd.DataFrame(np.reshape(X_topo, (6, 3))).to_csv('X_topo.csv')

        print('hi')
        """
        # Printing and ETC...
        headers = ['X(m)', 'Y(m)', 'Z(m)']
        table = [["GPS3", *X[0:3]], ["JACOBS", *X[3:6]], ["AB43", *X[6:9]],
                 ["PU29", *X[9:12]], ["MD13", *X[12:15]], ["30PU", *X[15:18]]]
        print(tabulate(table, headers, floatfmt=".4f", tablefmt="presto"))

        headers_topo = ['n(m)', 'e(m)', 'u(m)']
        table_topo = [["GPS3", *X_topo[0:3]], ["JACOBS", *X_topo[3:6]], ["AB43", *X_topo[6:9]],
                      ["PU29", *X_topo[9:12]], ["MD13", *X_topo[12:15]], ["30PU", *X_topo[15:18]]]
        print(tabulate(table_topo, headers_topo, floatfmt=".4f", tablefmt="presto"))

        filepath = 'D:\OneDrive\OneDrive - Technion\סמסטר 6\מדידות GPS\מעבדות\תוצאות עיבוד וקטור GPS\X_topo.xlsx'
        df = pd.DataFrame(X_topo)
        df.to_excel(filepath, index=False)
        """
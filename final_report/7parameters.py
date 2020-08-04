import numpy as np
import pandas as pd


def itm2GRS80(x, y, H):
    """
    for a given set of ITM IG05 coordinates, transform to geocentric coordinates on GRS80 (israel IND)
    :param x: N [m]
    :param y: E[m]
    :param H: orthometric height [m]
    :return: set of XYZ coordinates on GRS80 (israel IND)
    """
    ### define grs80 + itm parameters
    a = 6378137
    f = 1 / 298.2572222
    x0 = 626907.39
    y0 = 219529.584
    phi0 = np.radians(31 + 44 / 60 + 3.817 / 3600)
    lam0 = np.radians(35 + 12 / 60 + 16.261 / 3600)
    m0 = 1.0000067
    e = np.sqrt(2 * f - f * f)
    e_tag = np.sqrt(e * e / (1 - e * e))

    ### compute geographical coordinates in grs80
    ca = 1 + e * e * (3 / 4 + e * e * (45 / 64 + e * e * 175 / 256))
    cb = (e * e / 2) * (3 / 4 + e * e * (15 / 16 + e * e * 525 / 512))
    cc = (e * e * e * e / 4) * (15 / 64 + e * e * 105 / 256)
    cd = (e * e * e * e * e * e / 6) * 35 / 512

    sm = a * m0 * (1 - e * e) * (ca * phi0 - cb * np.sin(2 * phi0) + cc * np.sin(4 * phi0) - cd * np.sin(6 * phi0))

    dphi = 999
    phi1 = phi0
    while dphi > 1e-9:
        phi2 = (sm + (x - x0)) / (a * m0 * (1 - e * e) * ca) + (
                cb * np.sin(2 * phi1) - cc * np.sin(4 * phi1) + cd * np.sin(6 * phi1)) / ca
        dphi = np.abs(phi1 - phi2)
        phi1 = phi2

    n1 = (a * m0) / np.sqrt(1 - e * e * np.sin(phi1) ** 2)
    t1 = np.tan(phi1)
    eta1 = e_tag * np.cos(phi1)
    j = (y - y0) / n1

    phi = phi1 - t1 * (1 + eta1 * eta1) * (
            j * j / 2 - (j * j * j * j / 24) * (5 + 3 * t1 * t1 + eta1 * eta1 - 9 * t1 * t1 * eta1 * eta1))
    lam = lam0 + j * (1 - (j * j / 6) * (1 + 2 * t1 * t1 + eta1 * eta1) + (j * j * j * j / 120) * (
            5 + 28 * t1 * t1 + 24 * t1 * t1 * t1 * t1)) / np.cos(phi1)

    ### compute geocentrical coordinates in grs80 (using orthometric height)
    n = a / np.sqrt(1 - e * e * np.sin(phi) ** 2)
    X = (n + H) * np.cos(phi) * np.cos(lam)
    Y = (n + H) * np.cos(phi) * np.sin(lam)
    Z = (n * (1 - e * e) + H) * np.sin(phi)

    return np.array([[X], [Y], [Z]])


def seven_pars_adjustment(cp_wgs84, cp_grs80):



if __name__ == '__main__':
    # PU29, 30PU, MD13
    cp_itm = np.array([[743747.69, 740235.80, 741844.753], [202897.07, 202554.81, 200777.994],
                       [6.78, 438.49, 366.189]])  # known ITM coordinates
    cp_wgs84 = np.array([[4395103.335, 4397150.618, 4397410.255], [3080650.441, 3081674.605, 3079683.358],
                         [3434254.957, 3431535.182, 3432846.394]])  # computed with independent vectors

    cp_grs80 = []
    for p in cp_itm.T:
        cp_grs80.append(itm2GRS80(p[0], p[1], p[2]))

    cp_grs80 = np.hstack(cp_grs80)

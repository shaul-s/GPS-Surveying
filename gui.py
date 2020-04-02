# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import array, sqrt, sin, cos, deg2rad, rad2deg, arctan, pi, hstack, vstack, zeros, dot, linalg, arange, sort
from tabulate import tabulate


import matplotlib.pylab as plt

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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(1024, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("satellite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QGroupBox(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 10, 401, 661))
        self.input.setAlignment(QtCore.Qt.AlignCenter)
        self.input.setFlat(True)
        self.input.setCheckable(False)
        self.input.setObjectName("input")
        self.label = QtWidgets.QLabel(self.input)
        self.label.setGeometry(QtCore.QRect(20, 240, 101, 16))
        self.label.setObjectName("label")
        self.beta = QtWidgets.QLineEdit(self.input)
        self.beta.setGeometry(QtCore.QRect(140, 240, 81, 20))
        self.beta.setObjectName("beta")
        self.label_2 = QtWidgets.QLabel(self.input)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.input)
        self.label_3.setGeometry(QtCore.QRect(20, 340, 101, 16))
        self.label_3.setObjectName("label_3")
        self.begin_time = QtWidgets.QComboBox(self.input)
        self.begin_time.setGeometry(QtCore.QRect(140, 300, 69, 22))
        self.begin_time.setObjectName("begin_time")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.begin_time.addItem("")
        self.end_time = QtWidgets.QComboBox(self.input)
        self.end_time.setGeometry(QtCore.QRect(140, 340, 69, 22))
        self.end_time.setObjectName("end_time")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.end_time.addItem("")
        self.time_frame = QtWidgets.QFrame(self.input)
        self.time_frame.setGeometry(QtCore.QRect(10, 290, 311, 81))
        self.time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.time_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.time_frame.setObjectName("time_frame")
        self.beta_frame = QtWidgets.QFrame(self.input)
        self.beta_frame.setGeometry(QtCore.QRect(10, 230, 311, 41))
        self.beta_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.beta_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.beta_frame.setObjectName("beta_frame")
        self.label_19 = QtWidgets.QLabel(self.beta_frame)
        self.label_19.setGeometry(QtCore.QRect(220, 10, 51, 16))
        self.label_19.setObjectName("label_19")
        self.label_4 = QtWidgets.QLabel(self.input)
        self.label_4.setGeometry(QtCore.QRect(20, 410, 101, 16))
        self.label_4.setObjectName("label_4")
        self.base_station = QtWidgets.QComboBox(self.input)
        self.base_station.setGeometry(QtCore.QRect(140, 410, 51, 22))
        self.base_station.setObjectName("base_station")
        self.base_station.addItem("")
        self.base_station.setItemText(0, "")
        self.base_station.addItem("")
        self.base_station.addItem("")
        self.frame = QtWidgets.QFrame(self.input)
        self.frame.setGeometry(QtCore.QRect(10, 390, 311, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(240, 60, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(240, 90, 47, 13))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(240, 120, 47, 13))
        self.label_12.setObjectName("label_12")
        self.latit = QtWidgets.QLineEdit(self.input)
        self.latit.setEnabled(False)
        self.latit.setGeometry(QtCore.QRect(130, 450, 113, 20))
        self.latit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.latit.setObjectName("latit")
        self.longit = QtWidgets.QLineEdit(self.input)
        self.longit.setEnabled(False)
        self.longit.setGeometry(QtCore.QRect(130, 480, 113, 20))
        self.longit.setObjectName("longit")
        self.height = QtWidgets.QLineEdit(self.input)
        self.height.setEnabled(False)
        self.height.setGeometry(QtCore.QRect(130, 510, 113, 20))
        self.height.setObjectName("height")
        self.label_5 = QtWidgets.QLabel(self.input)
        self.label_5.setGeometry(QtCore.QRect(60, 450, 47, 13))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.input)
        self.label_6.setGeometry(QtCore.QRect(60, 480, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.input)
        self.label_7.setGeometry(QtCore.QRect(60, 510, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.input)
        self.label_8.setGeometry(QtCore.QRect(60, 450, 47, 13))
        self.label_8.setObjectName("label_8")
        self.calc = QtWidgets.QPushButton(self.input)
        self.calc.setGeometry(QtCore.QRect(10, 580, 111, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.calc.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.calc.setFont(font)
        self.calc.setFlat(False)
        self.calc.setObjectName("calc")
        self.frame_2 = QtWidgets.QFrame(self.input)
        self.frame_2.setGeometry(QtCore.QRect(10, 20, 311, 191))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(10, 130, 91, 16))
        self.label_13.setObjectName("label_13")
        self.sp3date = QtWidgets.QLineEdit(self.frame_2)
        self.sp3date.setEnabled(False)
        self.sp3date.setGeometry(QtCore.QRect(100, 130, 91, 20))
        self.sp3date.setObjectName("sp3date")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.label_14.setObjectName("label_14")
        self.num_sat = QtWidgets.QLineEdit(self.frame_2)
        self.num_sat.setEnabled(False)
        self.num_sat.setGeometry(QtCore.QRect(70, 90, 21, 20))
        self.num_sat.setObjectName("num_sat")
        self.of_dialog = QtWidgets.QPushButton(self.input)
        self.of_dialog.setGeometry(QtCore.QRect(20, 30, 91, 23))
        self.of_dialog.setObjectName("of_dialog")
        self.label_9 = QtWidgets.QLabel(self.input)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 47, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.input)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(50, 70, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.restart = QtWidgets.QPushButton(self.input)
        self.restart.setGeometry(QtCore.QRect(150, 580, 111, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.restart.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.restart.setFont(font)
        self.restart.setFlat(False)
        self.restart.setObjectName("restart")
        self.frame.raise_()
        self.beta_frame.raise_()
        self.time_frame.raise_()
        self.label.raise_()
        self.beta.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.begin_time.raise_()
        self.end_time.raise_()
        self.label_4.raise_()
        self.base_station.raise_()
        self.latit.raise_()
        self.longit.raise_()
        self.height.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.calc.raise_()
        self.frame_2.raise_()
        self.of_dialog.raise_()
        self.label_9.raise_()
        self.lineEdit.raise_()
        self.restart.raise_()
        self.results = QtWidgets.QGroupBox(self.centralwidget)
        self.results.setGeometry(QtCore.QRect(430, 10, 571, 661))
        self.results.setAlignment(QtCore.Qt.AlignCenter)
        self.results.setFlat(True)
        self.results.setObjectName("results")
        self.textBrowser = QtWidgets.QTextBrowser(self.results)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 531, 581))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.menuHelp.addAction(self.actionAbout_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.textBrowser.setAlignment(QtCore.Qt.AlignCenter)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Occupation Planning"))

        self.input.setTitle(_translate("MainWindow", "Input Data"))
        self.label.setText(_translate("MainWindow", "Critical Beta Angle:"))
        self.label_2.setText(_translate("MainWindow", "Select Beginning Time:"))
        self.label_3.setText(_translate("MainWindow", "Select End Time:"))
        self.begin_time.setItemText(0, _translate("MainWindow", "00:00"))
        self.begin_time.setItemText(1, _translate("MainWindow", "00:15"))
        self.begin_time.setItemText(2, _translate("MainWindow", "00:30"))
        self.begin_time.setItemText(3, _translate("MainWindow", "00:45"))
        self.begin_time.setItemText(4, _translate("MainWindow", "01:00"))
        self.begin_time.setItemText(5, _translate("MainWindow", "01:15"))
        self.begin_time.setItemText(6, _translate("MainWindow", "01:30"))
        self.begin_time.setItemText(7, _translate("MainWindow", "01:45"))
        self.begin_time.setItemText(8, _translate("MainWindow", "02:00"))
        self.begin_time.setItemText(9, _translate("MainWindow", "02:15"))
        self.begin_time.setItemText(10, _translate("MainWindow", "02:30"))
        self.begin_time.setItemText(11, _translate("MainWindow", "02:45"))
        self.begin_time.setItemText(12, _translate("MainWindow", "03:00"))
        self.begin_time.setItemText(13, _translate("MainWindow", "03:15"))
        self.begin_time.setItemText(14, _translate("MainWindow", "03:30"))
        self.begin_time.setItemText(15, _translate("MainWindow", "03:45"))
        self.begin_time.setItemText(16, _translate("MainWindow", "04:00"))
        self.begin_time.setItemText(17, _translate("MainWindow", "04:15"))
        self.begin_time.setItemText(18, _translate("MainWindow", "04:30"))
        self.begin_time.setItemText(19, _translate("MainWindow", "04:45"))
        self.begin_time.setItemText(20, _translate("MainWindow", "05:00"))
        self.begin_time.setItemText(21, _translate("MainWindow", "05:15"))
        self.begin_time.setItemText(22, _translate("MainWindow", "05:30"))
        self.begin_time.setItemText(23, _translate("MainWindow", "05:45"))
        self.begin_time.setItemText(24, _translate("MainWindow", "06:00"))
        self.begin_time.setItemText(25, _translate("MainWindow", "06:15"))
        self.begin_time.setItemText(26, _translate("MainWindow", "06:30"))
        self.begin_time.setItemText(27, _translate("MainWindow", "06:45"))
        self.begin_time.setItemText(28, _translate("MainWindow", "07:00"))
        self.begin_time.setItemText(29, _translate("MainWindow", "07:15"))
        self.begin_time.setItemText(30, _translate("MainWindow", "07:30"))
        self.begin_time.setItemText(31, _translate("MainWindow", "07:45"))
        self.begin_time.setItemText(32, _translate("MainWindow", "08:00"))
        self.begin_time.setItemText(33, _translate("MainWindow", "08:15"))
        self.begin_time.setItemText(34, _translate("MainWindow", "08:30"))
        self.begin_time.setItemText(35, _translate("MainWindow", "08:45"))
        self.begin_time.setItemText(36, _translate("MainWindow", "09:00"))
        self.begin_time.setItemText(37, _translate("MainWindow", "09:15"))
        self.begin_time.setItemText(38, _translate("MainWindow", "09:30"))
        self.begin_time.setItemText(39, _translate("MainWindow", "09:45"))
        self.begin_time.setItemText(40, _translate("MainWindow", "10:00"))
        self.begin_time.setItemText(41, _translate("MainWindow", "10:15"))
        self.begin_time.setItemText(42, _translate("MainWindow", "10:30"))
        self.begin_time.setItemText(43, _translate("MainWindow", "10:45"))
        self.begin_time.setItemText(44, _translate("MainWindow", "11:00"))
        self.begin_time.setItemText(45, _translate("MainWindow", "11:15"))
        self.begin_time.setItemText(46, _translate("MainWindow", "11:30"))
        self.begin_time.setItemText(47, _translate("MainWindow", "11:45"))
        self.begin_time.setItemText(48, _translate("MainWindow", "12:00"))
        self.begin_time.setItemText(49, _translate("MainWindow", "12:15"))
        self.begin_time.setItemText(50, _translate("MainWindow", "12:30"))
        self.begin_time.setItemText(51, _translate("MainWindow", "12:45"))
        self.begin_time.setItemText(52, _translate("MainWindow", "13:00"))
        self.begin_time.setItemText(53, _translate("MainWindow", "13:15"))
        self.begin_time.setItemText(54, _translate("MainWindow", "13:30"))
        self.begin_time.setItemText(55, _translate("MainWindow", "13:45"))
        self.begin_time.setItemText(56, _translate("MainWindow", "14:00"))
        self.begin_time.setItemText(57, _translate("MainWindow", "14:15"))
        self.begin_time.setItemText(58, _translate("MainWindow", "14:30"))
        self.begin_time.setItemText(59, _translate("MainWindow", "14:45"))
        self.begin_time.setItemText(60, _translate("MainWindow", "15:00"))
        self.begin_time.setItemText(61, _translate("MainWindow", "15:15"))
        self.begin_time.setItemText(62, _translate("MainWindow", "15:30"))
        self.begin_time.setItemText(63, _translate("MainWindow", "15:45"))
        self.begin_time.setItemText(64, _translate("MainWindow", "16:00"))
        self.begin_time.setItemText(65, _translate("MainWindow", "16:15"))
        self.begin_time.setItemText(66, _translate("MainWindow", "16:30"))
        self.begin_time.setItemText(67, _translate("MainWindow", "16:45"))
        self.begin_time.setItemText(68, _translate("MainWindow", "17:00"))
        self.begin_time.setItemText(69, _translate("MainWindow", "17:15"))
        self.begin_time.setItemText(70, _translate("MainWindow", "17:30"))
        self.begin_time.setItemText(71, _translate("MainWindow", "17:45"))
        self.begin_time.setItemText(72, _translate("MainWindow", "18:00"))
        self.begin_time.setItemText(73, _translate("MainWindow", "18:15"))
        self.begin_time.setItemText(74, _translate("MainWindow", "18:30"))
        self.begin_time.setItemText(75, _translate("MainWindow", "18:45"))
        self.begin_time.setItemText(76, _translate("MainWindow", "19:00"))
        self.begin_time.setItemText(77, _translate("MainWindow", "19:15"))
        self.begin_time.setItemText(78, _translate("MainWindow", "19:30"))
        self.begin_time.setItemText(79, _translate("MainWindow", "19:45"))
        self.begin_time.setItemText(80, _translate("MainWindow", "20:00"))
        self.begin_time.setItemText(81, _translate("MainWindow", "20:15"))
        self.begin_time.setItemText(82, _translate("MainWindow", "20:30"))
        self.begin_time.setItemText(83, _translate("MainWindow", "20:45"))
        self.begin_time.setItemText(84, _translate("MainWindow", "21:00"))
        self.begin_time.setItemText(85, _translate("MainWindow", "21:15"))
        self.begin_time.setItemText(86, _translate("MainWindow", "21:30"))
        self.begin_time.setItemText(87, _translate("MainWindow", "21:45"))
        self.begin_time.setItemText(88, _translate("MainWindow", "22:00"))
        self.begin_time.setItemText(89, _translate("MainWindow", "22:15"))
        self.begin_time.setItemText(90, _translate("MainWindow", "22:30"))
        self.begin_time.setItemText(91, _translate("MainWindow", "22:45"))
        self.begin_time.setItemText(92, _translate("MainWindow", "23:00"))
        self.begin_time.setItemText(93, _translate("MainWindow", "23:15"))
        self.begin_time.setItemText(94, _translate("MainWindow", "23:30"))
        self.begin_time.setItemText(95, _translate("MainWindow", "23:45"))
        self.end_time.setItemText(0, _translate("MainWindow", "00:00"))
        self.end_time.setItemText(1, _translate("MainWindow", "00:15"))
        self.end_time.setItemText(2, _translate("MainWindow", "00:30"))
        self.end_time.setItemText(3, _translate("MainWindow", "00:45"))
        self.end_time.setItemText(4, _translate("MainWindow", "01:00"))
        self.end_time.setItemText(5, _translate("MainWindow", "01:15"))
        self.end_time.setItemText(6, _translate("MainWindow", "01:30"))
        self.end_time.setItemText(7, _translate("MainWindow", "01:45"))
        self.end_time.setItemText(8, _translate("MainWindow", "02:00"))
        self.end_time.setItemText(9, _translate("MainWindow", "02:15"))
        self.end_time.setItemText(10, _translate("MainWindow", "02:30"))
        self.end_time.setItemText(11, _translate("MainWindow", "02:45"))
        self.end_time.setItemText(12, _translate("MainWindow", "03:00"))
        self.end_time.setItemText(13, _translate("MainWindow", "03:15"))
        self.end_time.setItemText(14, _translate("MainWindow", "03:30"))
        self.end_time.setItemText(15, _translate("MainWindow", "03:45"))
        self.end_time.setItemText(16, _translate("MainWindow", "04:00"))
        self.end_time.setItemText(17, _translate("MainWindow", "04:15"))
        self.end_time.setItemText(18, _translate("MainWindow", "04:30"))
        self.end_time.setItemText(19, _translate("MainWindow", "04:45"))
        self.end_time.setItemText(20, _translate("MainWindow", "05:00"))
        self.end_time.setItemText(21, _translate("MainWindow", "05:15"))
        self.end_time.setItemText(22, _translate("MainWindow", "05:30"))
        self.end_time.setItemText(23, _translate("MainWindow", "05:45"))
        self.end_time.setItemText(24, _translate("MainWindow", "06:00"))
        self.end_time.setItemText(25, _translate("MainWindow", "06:15"))
        self.end_time.setItemText(26, _translate("MainWindow", "06:30"))
        self.end_time.setItemText(27, _translate("MainWindow", "06:45"))
        self.end_time.setItemText(28, _translate("MainWindow", "07:00"))
        self.end_time.setItemText(29, _translate("MainWindow", "07:15"))
        self.end_time.setItemText(30, _translate("MainWindow", "07:30"))
        self.end_time.setItemText(31, _translate("MainWindow", "07:45"))
        self.end_time.setItemText(32, _translate("MainWindow", "08:00"))
        self.end_time.setItemText(33, _translate("MainWindow", "08:15"))
        self.end_time.setItemText(34, _translate("MainWindow", "08:30"))
        self.end_time.setItemText(35, _translate("MainWindow", "08:45"))
        self.end_time.setItemText(36, _translate("MainWindow", "09:00"))
        self.end_time.setItemText(37, _translate("MainWindow", "09:15"))
        self.end_time.setItemText(38, _translate("MainWindow", "09:30"))
        self.end_time.setItemText(39, _translate("MainWindow", "09:45"))
        self.end_time.setItemText(40, _translate("MainWindow", "10:00"))
        self.end_time.setItemText(41, _translate("MainWindow", "10:15"))
        self.end_time.setItemText(42, _translate("MainWindow", "10:30"))
        self.end_time.setItemText(43, _translate("MainWindow", "10:45"))
        self.end_time.setItemText(44, _translate("MainWindow", "11:00"))
        self.end_time.setItemText(45, _translate("MainWindow", "11:15"))
        self.end_time.setItemText(46, _translate("MainWindow", "11:30"))
        self.end_time.setItemText(47, _translate("MainWindow", "11:45"))
        self.end_time.setItemText(48, _translate("MainWindow", "12:00"))
        self.end_time.setItemText(49, _translate("MainWindow", "12:15"))
        self.end_time.setItemText(50, _translate("MainWindow", "12:30"))
        self.end_time.setItemText(51, _translate("MainWindow", "12:45"))
        self.end_time.setItemText(52, _translate("MainWindow", "13:00"))
        self.end_time.setItemText(53, _translate("MainWindow", "13:15"))
        self.end_time.setItemText(54, _translate("MainWindow", "13:30"))
        self.end_time.setItemText(55, _translate("MainWindow", "13:45"))
        self.end_time.setItemText(56, _translate("MainWindow", "14:00"))
        self.end_time.setItemText(57, _translate("MainWindow", "14:15"))
        self.end_time.setItemText(58, _translate("MainWindow", "14:30"))
        self.end_time.setItemText(59, _translate("MainWindow", "14:45"))
        self.end_time.setItemText(60, _translate("MainWindow", "15:00"))
        self.end_time.setItemText(61, _translate("MainWindow", "15:15"))
        self.end_time.setItemText(62, _translate("MainWindow", "15:30"))
        self.end_time.setItemText(63, _translate("MainWindow", "15:45"))
        self.end_time.setItemText(64, _translate("MainWindow", "16:00"))
        self.end_time.setItemText(65, _translate("MainWindow", "16:15"))
        self.end_time.setItemText(66, _translate("MainWindow", "16:30"))
        self.end_time.setItemText(67, _translate("MainWindow", "16:45"))
        self.end_time.setItemText(68, _translate("MainWindow", "17:00"))
        self.end_time.setItemText(69, _translate("MainWindow", "17:15"))
        self.end_time.setItemText(70, _translate("MainWindow", "17:30"))
        self.end_time.setItemText(71, _translate("MainWindow", "17:45"))
        self.end_time.setItemText(72, _translate("MainWindow", "18:00"))
        self.end_time.setItemText(73, _translate("MainWindow", "18:15"))
        self.end_time.setItemText(74, _translate("MainWindow", "18:30"))
        self.end_time.setItemText(75, _translate("MainWindow", "18:45"))
        self.end_time.setItemText(76, _translate("MainWindow", "19:00"))
        self.end_time.setItemText(77, _translate("MainWindow", "19:15"))
        self.end_time.setItemText(78, _translate("MainWindow", "19:30"))
        self.end_time.setItemText(79, _translate("MainWindow", "19:45"))
        self.end_time.setItemText(80, _translate("MainWindow", "20:00"))
        self.end_time.setItemText(81, _translate("MainWindow", "20:15"))
        self.end_time.setItemText(82, _translate("MainWindow", "20:30"))
        self.end_time.setItemText(83, _translate("MainWindow", "20:45"))
        self.end_time.setItemText(84, _translate("MainWindow", "21:00"))
        self.end_time.setItemText(85, _translate("MainWindow", "21:15"))
        self.end_time.setItemText(86, _translate("MainWindow", "21:30"))
        self.end_time.setItemText(87, _translate("MainWindow", "21:45"))
        self.end_time.setItemText(88, _translate("MainWindow", "22:00"))
        self.end_time.setItemText(89, _translate("MainWindow", "22:15"))
        self.end_time.setItemText(90, _translate("MainWindow", "22:30"))
        self.end_time.setItemText(91, _translate("MainWindow", "22:45"))
        self.end_time.setItemText(92, _translate("MainWindow", "23:00"))
        self.end_time.setItemText(93, _translate("MainWindow", "23:15"))
        self.end_time.setItemText(94, _translate("MainWindow", "23:30"))
        self.end_time.setItemText(95, _translate("MainWindow", "23:45"))
        self.label_19.setText(_translate("MainWindow", "degrees"))
        self.label_4.setText(_translate("MainWindow", "Select Base Station:"))
        self.base_station.setItemText(1, _translate("MainWindow", "BSHM"))
        self.base_station.setItemText(2, _translate("MainWindow", "ELAT"))
        self.label_10.setText(_translate("MainWindow", "DMS"))
        self.label_11.setText(_translate("MainWindow", "DMS"))
        self.label_12.setText(_translate("MainWindow", "meters"))
        self.label_6.setText(_translate("MainWindow", "Longitude:"))
        self.label_7.setText(_translate("MainWindow", "Height:"))
        self.label_8.setText(_translate("MainWindow", "Latitude:"))
        self.calc.setText(_translate("MainWindow", "Calculate"))
        self.label_13.setText(_translate("MainWindow", "Date for this SP3:"))
        self.label_14.setText(_translate("MainWindow", "#Satellites:"))
        self.of_dialog.setText(_translate("MainWindow", "Browse SP3 file"))
        self.label_9.setText(_translate("MainWindow", "Path:"))
        self.restart.setText(_translate("MainWindow", "Restart"))
        self.results.setTitle(_translate("MainWindow", "Results"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
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
                    and lines[j].rstrip('\n') != '*  {}  {} {}  {}  {}  0.00000000'.format(str(date[2]), str(date[1]),
                                                                                      str(date[0]), str(end_time[0]),
                                                                                      str(end_time[1])) \
                    and lines[j].rstrip('\n') != '*  {}  {} {} {}  {}  0.00000000'.format(str(date[2]), str(date[1]),
                                                                                     str(date[0]), str(end_time[0]),
                                                                                     str(end_time[1])) \
                    and lines[j].rstrip('\n') != '*  {}  {} {}  {} {}  0.00000000'.format(str(date[2]), str(date[1]),
                                                                                     str(date[0]), str(end_time[0]),
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
        x = arange(time[0][0], time[-1][0], 0.25)
        y = results[:, 1].astype(int)
        sort(y)
        plt.plot(x, y)
        plt.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

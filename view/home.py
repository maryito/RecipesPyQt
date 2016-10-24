# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_home(object):
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(800, 650)
        home.setMinimumSize(QtCore.QSize(800, 650))
        home.setMaximumSize(QtCore.QSize(800, 650))
        self.centralwidget = QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 611, 61))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 90, 691, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.panel = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.panel.setContentsMargins(50, 25, 50, 25)
        self.panel.setSpacing(3)
        self.panel.setObjectName("panel")
        self.bt_list_rec = QtWidgets.QPushButton(self.centralwidget)
        self.bt_list_rec.setGeometry(QtCore.QRect(190, 470, 431, 71))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.bt_list_rec.setFont(font)
        self.bt_list_rec.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.bt_list_rec.setObjectName("bt_list_rec")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 580, 271, 31))
        self.label_2.setObjectName("label_2")
        home.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(home)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans L")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.statusbar.setFont(font)
        self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.statusbar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusbar.setAutoFillBackground(True)
        self.statusbar.setObjectName("statusbar")
        home.setStatusBar(self.statusbar)
        self.actionActualizar = QtWidgets.QAction(home)
        self.actionActualizar.setObjectName("actionActualizar")
        self.actionVer_Listado = QtWidgets.QAction(home)
        self.actionVer_Listado.setObjectName("actionVer_Listado")

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "Home Recetas "))
        self.label.setText(_translate("home", "BIENVENIDOS A RECETAS AL DÍA"))
        self.bt_list_rec.setText(_translate("home", "Catalogo De Recetas"))
        self.label_2.setText(_translate("home", "Desarrollado Por Maryon J. Torres R"))
        self.actionActualizar.setText(_translate("home", "Actualizar"))
        self.actionVer_Listado.setText(_translate("home", "Ver Listado"))


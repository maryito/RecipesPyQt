# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recipes.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(800, 700)
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        MainWindow.setMaximumSize(QtCore.QSize(800, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(50, 230, 711, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(18)
        self.titulo.setFont(font)
        self.titulo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(500, 290, 261, 146))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.icon1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.icon1.setObjectName("icon1")
        self.horizontalLayout.addWidget(self.icon1)
        self.time = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.time.setMinimumSize(QtCore.QSize(200, 0))
        self.time.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.time.setFont(font)
        self.time.setObjectName("time")
        self.horizontalLayout.addWidget(self.time)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.icon2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.icon2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.icon2.setObjectName("icon2")
        self.horizontalLayout_2.addWidget(self.icon2)
        self.time_p = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.time_p.setMinimumSize(QtCore.QSize(200, 0))
        self.time_p.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.time_p.setFont(font)
        self.time_p.setObjectName("time_p")
        self.horizontalLayout_2.addWidget(self.time_p)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.list_img = QtWidgets.QLabel(self.centralwidget)
        self.list_img.setGeometry(QtCore.QRect(200, 10, 400, 200))
        self.list_img.setMinimumSize(QtCore.QSize(400, 200))
        self.list_img.setMaximumSize(QtCore.QSize(400, 200))
        self.list_img.setAlignment(QtCore.Qt.AlignCenter)
        self.list_img.setObjectName("list_img")
        self.list_recteas = QtWidgets.QTreeWidget(self.centralwidget)
        self.list_recteas.setGeometry(QtCore.QRect(30, 270, 431, 191))
        self.list_recteas.setObjectName("list_recteas")
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.list_recteas.headerItem().setFont(0, font)
        self.list_instruc = QtWidgets.QTreeWidget(self.centralwidget)
        self.list_instruc.setGeometry(QtCore.QRect(40, 470, 731, 211))
        self.list_instruc.setObjectName("list_instruc")
        self.list_instruc.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.list_instruc.headerItem().setFont(0, font)
        self.list_instruc.headerItem().setBackground(0, QtGui.QColor(0, 85, 255))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Informacion de Receta"))
        self.titulo.setText(_translate("MainWindow", "TITULO DE LA RECETA"))
        self.icon1.setText(_translate("MainWindow", "icon"))
        self.time.setText(_translate("MainWindow", "Tiempo"))
        self.icon2.setText(_translate("MainWindow", "icon"))
        self.time_p.setText(_translate("MainWindow", "Preparacion"))
        self.list_img.setText(_translate("MainWindow", "IMAGEN"))
        self.list_recteas.headerItem().setText(0, _translate("MainWindow", "INGREDIENTES"))
        self.list_instruc.headerItem().setText(0, _translate("MainWindow", "INSTRUCIONES"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.minButton = QtWidgets.QPushButton(self.centralwidget)
        self.minButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minButton.setIcon(icon)
        self.minButton.setIconSize(QtCore.QSize(25, 25))
        self.minButton.setFlat(True)
        self.minButton.setObjectName("minButton")
        self.horizontalLayout_4.addWidget(self.minButton)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon1)
        self.closeButton.setIconSize(QtCore.QSize(25, 25))
        self.closeButton.setFlat(True)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_4.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.memberButton = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.memberButton.setFont(font)
        self.memberButton.setObjectName("memberButton")
        self.horizontalLayout.addWidget(self.memberButton)
        self.scoreButton = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.scoreButton.setFont(font)
        self.scoreButton.setChecked(True)
        self.scoreButton.setObjectName("scoreButton")
        self.horizontalLayout.addWidget(self.scoreButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.pathLineEdit.setFont(font)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.horizontalLayout_2.addWidget(self.pathLineEdit)
        self.selectPathButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.selectPathButton.setFont(font)
        self.selectPathButton.setObjectName("selectPathButton")
        self.horizontalLayout_2.addWidget(self.selectPathButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout_3.addWidget(self.confirmButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.minButton.clicked.connect(MainWindow.showMinimized)
        self.closeButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.memberButton.setText(_translate("MainWindow", "人员名单导入"))
        self.scoreButton.setText(_translate("MainWindow", "积分变更导入"))
        self.selectPathButton.setText(_translate("MainWindow", "..."))
        self.confirmButton.setText(_translate("MainWindow", "导入"))
import res_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rf/PycharmProjects/sbrys/ui/qtd_main.ui'
#
# Created: Tue Jan 30 22:34:08 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_sbrys_main_qw(object):
    def setupUi(self, sbrys_main_qw):
        sbrys_main_qw.setObjectName("sbrys_main_qw")
        sbrys_main_qw.resize(936, 749)
        self.verticalLayout_2 = QtGui.QVBoxLayout(sbrys_main_qw)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtGui.QComboBox(sbrys_main_qw)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.sbrys_lineE = QtGui.QLineEdit(sbrys_main_qw)
        self.sbrys_lineE.setObjectName("sbrys_lineE")
        self.gridLayout.addWidget(self.sbrys_lineE, 0, 1, 1, 1)
        self.radioButton = QtGui.QRadioButton(sbrys_main_qw)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(sbrys_main_qw)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(sbrys_main_qw)
        QtCore.QMetaObject.connectSlotsByName(sbrys_main_qw)

    def retranslateUi(self, sbrys_main_qw):
        sbrys_main_qw.setWindowTitle(QtGui.QApplication.translate("sbrys_main_qw", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("sbrys_main_qw", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("sbrys_main_qw", "PushButton", None, QtGui.QApplication.UnicodeUTF8))


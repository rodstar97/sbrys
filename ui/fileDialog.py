# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rf/PycharmProjects/sbrys/ui/fileDialog.ui'
#
# Created: Sun Feb 11 20:43:18 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_create_sbrys_file(object):
    def setupUi(self, create_sbrys_file):
        create_sbrys_file.setObjectName("create_sbrys_file")
        create_sbrys_file.resize(676, 743)
        self.verticalLayout = QtGui.QVBoxLayout(create_sbrys_file)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toHide = QtGui.QPushButton(create_sbrys_file)
        self.toHide.setEnabled(False)
        self.toHide.setAutoDefault(False)
        self.toHide.setDefault(True)
        self.toHide.setObjectName("toHide")
        self.verticalLayout.addWidget(self.toHide)
        self.label = QtGui.QLabel(create_sbrys_file)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.name_le = QtGui.QLineEdit(create_sbrys_file)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_le.sizePolicy().hasHeightForWidth())
        self.name_le.setSizePolicy(sizePolicy)
        self.name_le.setObjectName("name_le")
        self.verticalLayout.addWidget(self.name_le)
        self.label_4 = QtGui.QLabel(create_sbrys_file)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_2 = QtGui.QLabel(create_sbrys_file)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(30, 0))
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tag_hl = QtGui.QHBoxLayout()
        self.tag_hl.setSpacing(6)
        self.tag_hl.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.tag_hl.setObjectName("tag_hl")
        self.verticalLayout.addLayout(self.tag_hl)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tags_le = QtGui.QLineEdit(create_sbrys_file)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tags_le.sizePolicy().hasHeightForWidth())
        self.tags_le.setSizePolicy(sizePolicy)
        self.tags_le.setMinimumSize(QtCore.QSize(0, 0))
        self.tags_le.setObjectName("tags_le")
        self.horizontalLayout.addWidget(self.tags_le)
        self.add_tag_pb = QtGui.QPushButton(create_sbrys_file)
        self.add_tag_pb.setAutoDefault(True)
        self.add_tag_pb.setDefault(False)
        self.add_tag_pb.setObjectName("add_tag_pb")
        self.horizontalLayout.addWidget(self.add_tag_pb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_6 = QtGui.QLabel(create_sbrys_file)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_3 = QtGui.QLabel(create_sbrys_file)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.desr_le = QtGui.QLineEdit(create_sbrys_file)
        self.desr_le.setObjectName("desr_le")
        self.verticalLayout.addWidget(self.desr_le)
        self.label_7 = QtGui.QLabel(create_sbrys_file)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_5 = QtGui.QLabel(create_sbrys_file)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.textEdit = QtGui.QTextEdit(create_sbrys_file)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.label_8 = QtGui.QLabel(create_sbrys_file)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.image_pb = QtGui.QPushButton(create_sbrys_file)
        self.image_pb.setObjectName("image_pb")
        self.verticalLayout.addWidget(self.image_pb)
        self.buttonBox = QtGui.QDialogButtonBox(create_sbrys_file)
        self.buttonBox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(create_sbrys_file)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), create_sbrys_file.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), create_sbrys_file.reject)
        QtCore.QMetaObject.connectSlotsByName(create_sbrys_file)
        create_sbrys_file.setTabOrder(self.name_le, self.tags_le)
        create_sbrys_file.setTabOrder(self.tags_le, self.add_tag_pb)
        create_sbrys_file.setTabOrder(self.add_tag_pb, self.desr_le)
        create_sbrys_file.setTabOrder(self.desr_le, self.textEdit)
        create_sbrys_file.setTabOrder(self.textEdit, self.image_pb)
        create_sbrys_file.setTabOrder(self.image_pb, self.buttonBox)
        create_sbrys_file.setTabOrder(self.buttonBox, self.toHide)

    def retranslateUi(self, create_sbrys_file):
        create_sbrys_file.setWindowTitle(QtGui.QApplication.translate("create_sbrys_file", "create sbrys", None, QtGui.QApplication.UnicodeUTF8))
        self.toHide.setText(QtGui.QApplication.translate("create_sbrys_file", "stupid Trick", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("create_sbrys_file", "name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("create_sbrys_file", "name should make sense , please no spaces", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("create_sbrys_file", "tags:", None, QtGui.QApplication.UnicodeUTF8))
        self.add_tag_pb.setText(QtGui.QApplication.translate("create_sbrys_file", "add Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("create_sbrys_file", "space seperated ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("create_sbrys_file", "description short:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("create_sbrys_file", "short description what your  stuff is doing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("create_sbrys_file", "discription long:", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("create_sbrys_file", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Yeah  its anoying , but your future self will love you</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("create_sbrys_file", "if you share sbrys files, this should make sense how to use your nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.image_pb.setText(QtGui.QApplication.translate("create_sbrys_file", "create Snapshot", None, QtGui.QApplication.UnicodeUTF8))


from ui.fileDialog import Ui_create_sbrys_file
from PySide import QtCore, QtGui

tag_list = ['test','maya','houdini','mari','nuke']
predefined_tag_list = ['maya', 'hypershade', 'shader']

class TagButton(QtGui.QPushButton):

    # create Signals for DoubleClick remove
    doubleClicked = QtCore.Signal()
    clicked = QtCore.Signal()

    def __init__(self, name):
        super(TagButton, self).__init__()

        self.name = name
        self.setFixedHeight(20)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setText(self.name)
        self.newfont = QtGui.QFont("Ubuntu", 7, QtGui.QFont.Normal)
        self.setFont(self.newfont)
        self.setStyleSheet("background-color:rgba(12,125,35,125);"
                           "border-width: 5px;border-radius: 10px;")

        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.clicked.emit)
        self.clicked.connect(self.checkDoubleClick)
        self.doubleClicked.connect(self.remove_button)

    @QtCore.Slot()
    def checkDoubleClick(self):
        if self.timer.isActive():
            self.doubleClicked.emit()
            self.timer.stop()
        else:
            self.timer.start(250)


    def remove_button(self):
        self.deleteLater()






class CreateSbrysFile(QtGui.QDialog):
    def __init__(self):
        super(CreateSbrysFile, self).__init__()
        self.ui = Ui_create_sbrys_file()
        self.ui.setupUi(self)


        #set auto completion in tags
        self.completer = QtGui.QCompleter()
        self.ui.tags_le.setCompleter(self.completer)
        self.model = QtGui.QStringListModel()
        self.completer.setModel(self.model)
        self.get_data(self.model)

        self.add_predifined_tags()
        self.ui.add_tag_pb.clicked.connect(self.add_tag_to_taglist)
        self.ui.toHide.hide()
        #self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setAutoDefault(False)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setDefault(False)#setToolTip('Apply Tooltip')#button(QtGui.QDialogButtonBox.OK).setAutoFocus(False)


    def get_data(self, model, list=[]):
        #toDo filter out predifined Tags
        model.setStringList(tag_list)

    def add_predifined_tags(self, list=[]):
        for tag in predefined_tag_list:
            self.ui.tag_hl.addWidget(TagButton(name=tag))

    def add_tag_to_taglist(self):
        print 'ahha'
        self.ui.tags_le.text()
        self.ui.tag_hl.addWidget(TagButton(name=self.ui.tags_le.text()))
        self.ui.tags_le.setText('')







if __name__ == '__main__':
    import sys, os
    from utils.convert_ui_files import convert


    '''Convert UI Files'''
    pwd = os.path.dirname(os.path.realpath(__file__))
    ui_files = os.path.join(pwd, 'ui')
    print ui_files
    convert(ui_files)

    '''Show GUI'''
    app = QtGui.QApplication(sys.argv)
    myWidget = CreateSbrysFile()
    myWidget.show()
    app.exec_()
from ui.fileDialog import Ui_create_sbrys_file
from PySide import QtCore, QtGui
from extra_widgets import FlowLayout
from screen_shot import SnapshotWidget
tag_list = ['test','maya','houdini','mari','nuke']
predefined_tag_list = ['maya', 'hypershade', 'shader']




class TagButton(QtGui.QPushButton):
    """"
    Button based on QPushButton
    Fixed size detroys self by double Click

    """

    # create Signals for DoubleClick remove
    doubleClicked = QtCore.Signal()
    clicked = QtCore.Signal()

    def __init__(self, name):
        super(TagButton, self).__init__()

        self.name = name
        self.setFixedHeight(20)
        self.setMinimumWidth(70)
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


class SbrysLineEdit(QtGui.QLineEdit):
    """
        Adabtation from QLineEdit
        add Multi Tag autoComplition

    """
    def __init__(self, *args, **kwargs):
        QtGui.QLineEdit.__init__(self, *args, **kwargs)
        self.multipleCompleter = None

    def keyPressEvent(self, event):
        QtGui.QLineEdit.keyPressEvent(self, event)
        if not self.multipleCompleter:
            return
        c = self.multipleCompleter
        if self.text() == "":
            return
        c.setCompletionPrefix(self.cursorWord(self.text()))
        if len(c.completionPrefix()) < 1:
            c.popup().hide()
            return
        c.complete()

    def cursorWord(self, sentence):
        p = sentence.rfind(" ")
        if p == -1:
            return sentence
        return sentence[p + 1:]

    def insertCompletion(self, text):
        p = self.text().rfind(" ")
        if p == -1:
            self.setText(text)
        else:
            self.setText(self.text()[:p+1]+ text)

    def setMultipleCompleter(self, completer):
        self.multipleCompleter = completer
        self.multipleCompleter.setWidget(self)
        completer.activated.connect(self.insertCompletion)





class CreateSbrysFile(QtGui.QDialog):
    """
        QFileDialog Collect Infos for File saving

    """

    def __init__(self):
        super(CreateSbrysFile, self).__init__()
        self.ui = Ui_create_sbrys_file()
        self.ui.setupUi(self)
        self.ui.image_pb.clicked.connect(self.create_snapShot)

        # setup for Tags in flowLayout
        self.tags_le = SbrysLineEdit()
        self.tags_le.setObjectName('tags_le')
        self.tags_flw = QtGui.QWidget()
        self.tags_fl = FlowLayout()
        self.tags_flw.setLayout(self.tags_fl)
        self.ui.tag_buttons_hl.addWidget(self.tags_flw)

        #set auto completion in tags
        self.completer = QtGui.QCompleter()
        self.tags_le.setMultipleCompleter(self.completer)
        self.model = QtGui.QStringListModel()
        self.completer.setModel(self.model)
        self.get_data(self.model)

        #fill tag list
        self.add_predifined_tags()
        self.ui.add_tag_pb.clicked.connect(self.add_tag_to_taglist)
        self.ui.toHide.hide()
        self.ui.tags_hl.insertWidget(0, self.tags_le, 0)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setDefault(False)

        #set Tab Order
        self.set_tab_order()

    def get_data(self, model, list=[]):
        #toDo filter out predifined Tags
        model.setStringList(tag_list)


    def add_predifined_tags(self, list=[]):
        for tag in predefined_tag_list:
            self.tags_fl.addWidget(TagButton(name=tag))


    def add_tag_to_taglist(self):
        #toDO better testing that no Tags with Spaces or emty Tags are allowed
        if self.tags_le.text() != "":
            for tag in self.tags_le.text().split(" "):
                self.tags_fl.addWidget(TagButton(name=tag))
                self.tags_le.setText('')


    def set_tab_order(self):
        """
        Set tab Order by tab orderlist
        """
        self.tab_order_list = ['name_le','tags_le','add_tag_pb','desr_le','desc_long_te','image_pb']
        self.short_name_obj_matrix={
            'le':QtGui.QLineEdit,
            'pb':QtGui.QPushButton,
            'te':QtGui.QTextEdit
        }
        for index in xrange(len((self.tab_order_list))-1):
            index_name = self.tab_order_list[index]
            next_name =  self.tab_order_list[index+1]
            index_widget = self.findChild(self.short_name_obj_matrix[index_name.split('_')[-1]], index_name)
            next_widget  = self.findChild(self.short_name_obj_matrix[next_name.split('_')[-1]], next_name)

            self.setTabOrder(index_widget, next_widget)


    def create_snapShot(self):
        self.snapshot_widget = SnapshotWidget().get_data()
        self.ui.image_pb.setIcon(self.snapshot_widget)
        self.ui.image_pb.setIconSize(QtCore.QSize(230, 230))

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
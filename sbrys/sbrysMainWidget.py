from PySide import QtCore, QtGui
from ui.qtd_main import Ui_sbrys_main_qw
from extra_widgets import FlowLayout

'''
Keep this in a widget you can direct use it in Houdini


'''


class MainItemLayoutWidget(QtGui.QWidget):

    def __init__(self):
        super(MainItemLayoutWidget, self).__init__()
        self.scrollLayout = FlowLayout()#QtGui.QFormLayout()
        for i in xrange(20):
            self.scrollLayout.addWidget(QtGui.QPushButton())
        # scroll area widget contents
        self.scrollWidget = QtGui.QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)

        # scroll area
        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)
        self.mainLayout = QtGui.QVBoxLayout()

        # add all main to the main vLayout

        self.mainLayout.addWidget(self.scrollArea)
        self.centralWidget = QtGui.QWidget()
        self.setLayout(self.mainLayout)

    def add_widget(self):
        self.scrollLayout.addWidget(QtGui.QPushButton('test'))  # addRow(Test())

        # set central widget
        #self.setCentralWidget(self.centralWidget)




class MainWidget(Ui_sbrys_main_qw, QtGui.QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.itemLayout = MainItemLayoutWidget()

        self.setupUi(self)
        self.create_flowLayout()




    def create_flowLayout(self):
        '''
        self.layout = QtGui.QVBoxLayout()
        for i in xrange(20):
            self.layout.addWidget(QtGui.QPushButton('test_{0}'.format(i)))
        self.flowlayout_null.setLayout(self.layout)
        '''

        for i in xrange(20):
            self.itemLayout.add_widget()
        self.verticalLayout.addWidget(self.itemLayout)#self.itemLayout




if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    myWidget = MainWidget()
    myWidget.show()
    app.exec_()
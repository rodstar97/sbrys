from PySide import QtCore, QtGui
import sys, os

class ComponentWidget(QtGui.QWidget):
    def __init__(self, path='', selected = False,
                 icon ='', parent = None ):
        super(ComponentWidget, self).__init__(parent)
        #self.setupUi(path=path)
        #if selected:
            #self.change_color()
        self.layout = QtGui.QHBoxLayout()
        self.layout.addWidget(QtGui.QPushButton('TEST'))
        self.setLayout(self.layout)





'''
    def setupUi(self, path):
        #type = component_matrix(path)
        #layout
        self.layout = QtGui.QHBoxLayout(self)
        #icon
        self.icon = QtGui.QLabel()
        self.icon.setMaximumSize(QtCore.QSize(24, 24))
        #self.icon.setPixmap(self.set_icon('icons/{0}.png'.format(type)))
        self.icon.setScaledContents(True)
        #name
        self.name = QtGui.QLabel(type)

        #Path to Component
        self.path = QtGui.QLineEdit(self)
        self.path.setText(path)
        self.path.setReadOnly(True)

        #set Widgets
        self.layout.addWidget(self.icon)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.path)

    def set_icon(self, path=''):
        return QtGui.QPixmap(path)

    def change_color(self):
        color = self.palette().highlight().color().name()
        self.setStyleSheet("background-color:{0};".format(color))
        '''
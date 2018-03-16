from PySide import QtGui, QtCore
import sys, random


class FlowListModel(QtCore.QAbstractListModel):
    '''
        Generate the data Structure and How List View or other Views see this data

    '''

    def __init__(self, colors=[]):
        super(FlowListModel, self).__init__()
        self._colors = colors

    def rowCount(self, parent):
        return len(self._colors)


    def data(self, index, role,):
        if role == QtCore.Qt.DisplayRole:
            #return 'HardCodedINput could be a\n litel longer what happen then'#self._colors[index]
            return '{0}'.format(self._colors[index.row()])

        elif role == QtCore.Qt.DecorationRole:
            pixmap = QtGui.QPixmap(100, 100)
            pixmap.fill(QtGui.QColor(self._colors[index.row()],self._colors[index.row()],self._colors[index.row()]))

            icon = QtGui.QIcon(pixmap)

            return icon

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable



class FlowListView(QtGui.QListView):
    '''
        Inherit List View for FlowLayout behavoir


    '''

    def __init__(self, parent=None, *args):
        super(FlowListView, self).__init__(parent=parent, *args)


        # size

        self.setIconSize(QtCore.QSize(100, 100))

        self.setSpacing(5)
        self.setUniformItemSizes(True)
        self.setViewMode(QtGui.QListView.IconMode)
        self.setFlow(QtGui.QListView.LeftToRight)
        self.setWrapping(1)
        self.setResizeMode(QtGui.QListView.Adjust)

        #self.setDragDropMode(QtGui.QAbstractItemView.InternalMove);
        #self.customContextMenuRequested.connect(self.onContext)

    def onContext(self):
        # Create a menu
        menu = QtGui.QMenu("Menu", self)
        menu.addAction(self.mAction1)
        menu.addAction(self.mAction2)
        # Show the context menu.
        menu.exec_(QtCore.Qt.view.mapToGlobal(point))






if __name__ == '__main__':


    app = QtGui.QApplication(sys.argv)
    #create and show list view
    listView = FlowListView()#QtGui.QListView()#


    #create Model

    #create Colors

    red   = QtGui.QColor(255,0,0)
    green = QtGui.QColor(0,255,0)
    blue  = QtGui.QColor(0,0,255)

    number_of_items =[]
    for i in range(1000):
        number_of_items.append(random.randint(0,255))

    model = FlowListModel(number_of_items)#[red, green, blue])
    listView.setModel(model)


    listView.show()
    sys.exit(app.exec_())
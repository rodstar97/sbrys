from PySide import QtGui, QtCore
import sys



class FlowListModel(QtCore.QAbstractListModel):

    def __init__(self, colors=[]):
        super(FlowListModel, self).__init__()
        self._colors = colors

    def rowCount(self, parent):
        return len(self._colors)

    """
    def data(self, index, role,):
    """


class FlowListView(QtGui.QListView):
    def __init__(self, parent=None, *args):
        super(FlowListView, self).__init__(parent=parent, *args)


        # size
        '''
        self.setIconSize(QtCore.QSize(50, 50))

        self.setSpacing(5)
        self.setUniformItemSizes(True)
        self.setViewMode(QtGui.QListView.IconMode)
        self.setFlow(QtGui.QListView.LeftToRight)
        self.setWrapping(1)
        self.setResizeMode(QtGui.QListView.Adjust)
        '''







if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    #create and show list view
    listView = QtGui.QListView()#FlowListView()
    listView.show()

    #create Model

    #create Colors

    red   = QtGui.QColor(255,0,0)
    green = QtGui.QColor(0,255,0)
    blue  = QtGui.QColor(0,0,255)

    model = FlowListModel([red, green, blue])
    listView.setModel(model)



    sys.exit(app.exec_())
import sys, os
from PySide import QtGui, QtCore


class Selector(QtGui.QRubberBand):
    def __init__(self,*arg,**kwargs):
        super(Selector, self).__init__(*arg, **kwargs)

        self.setStyle(QtGui.QStyleFactory.create('windowsvista'))

    #toDo
    #def paintEvent(self, QPaintEvent):
        #pass
        #find some way to Keep Rubberband Selection in All Os and styles the Same "perhaps Style Sheets "



class GetSelection(QtGui.QLabel):
    def __init__ (self, parent = None):
        super(GetSelection, self).__init__(parent)
        self.setMouseTracking(True)
        self.coloring = QtGui.QGraphicsColorizeEffect()
        self.rubberBand = Selector(QtGui.QRubberBand.Rectangle,self)
        self.origin = QtCore.QPoint()


    def mouseMoveEvent (self, eventQMouseEvent):
        if not self.origin.isNull():
            self.rubberBand.setGeometry(QtCore.QRect(self.origin, eventQMouseEvent.pos()).normalized())

    def mousePressEvent (self, eventQMouseEvent):
        if eventQMouseEvent.button() == QtCore.Qt.LeftButton:
            self.origin = QtCore.QPoint(eventQMouseEvent.pos())
            self.rubberBand.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
            self.rubberBand.show()


    def mouseReleaseEvent(self, eventQMouseEvent):
        if eventQMouseEvent.button() == QtCore.Qt.LeftButton:
            #self.parent().setWindowOpacity(0.0)
            self.rubberBand.hide()
            self.parent().selection = self.rubberBand.geometry()
            self.parent().close()







class SnapshotWidget (QtGui.QDialog):#QtGui.QDialog
    def __init__ (self, parent = None):
        super(SnapshotWidget, self).__init__(parent)

        self.selection = []
        self.setWindowOpacity(0.9)
        # Init QLabel
        self.positionQLabel = GetSelection(self)

        self.setWindowState(QtCore.Qt.WindowFullScreen)

        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        #self.setWindowModality(QtCore.Qt.ApplicationModal)

        # Init QLayout
        layoutQHBoxLayout = QtGui.QHBoxLayout()
        layoutQHBoxLayout.addWidget(self.positionQLabel)
        self.setLayout(layoutQHBoxLayout)
        self.showFullScreen()

    def keyPressEvent(self, event):
        # Re-direct ESC key to closeEvent
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()



    @staticmethod
    def get_data(parent=None):
        dialog = SnapshotWidget(parent)
        dialog.exec_()
        appInstance = QtCore.QCoreApplication.instance()
        screen = appInstance.desktop().winId()
        print  dialog.selection.getRect()
        set_selection = ((dialog.selection.getRect()[0]+11), (dialog.selection.getRect()[1]+11),(dialog.selection.getRect()[2]),(dialog.selection.getRect()[3]))

        screenshot = QtGui.QPixmap.grabWindow(screen, *set_selection)#*(dialog.selection.getRect()
        return screenshot


class TestSS(QtGui.QMainWindow):
    def __init__(self):
        super(TestSS,self).__init__()
        self.qlayout = QtGui.QHBoxLayout()
        #self.menuBar.hide()
        self.button = QtGui.QPushButton('create SnapShot')

        self.button.clicked.connect(self.createSnapShot)
        self.qlayout.addWidget(self.button)
        self.setCentralWidget(self.button)
        #self.setWindowModality(QtCore.Qt.WindowModal)

    def createSnapShot(self):
        self.snapshot_widget = SnapshotWidget().get_data()
        #self.snapshot_widget.setWindowModality(QtCore.Qt.WindowModal)
        #self.snapshot_widget.setWindowModality(QtCore.Qt.ApplicationModal)
        #self.snapshot_widget.exec_()
        self.button.setIcon(self.snapshot_widget)
        #self.setIconSize(self.button.size())
        self.button.setIconSize(QtCore.QSize(230, 230))
        #self.button.setGeometry(QtCore.QRect(1030, 500, 161, 61))





if __name__ == '__main__':




    app = QtGui.QApplication(sys.argv)
    myQTestWidget = TestSS()


    #myQTestWidget.setWindowModality(QtCore.Qt.ApplicationModal)
    myQTestWidget.show()

    #screen = app.desktop().winId()
    ##screenshot.save(os.path.expanduser("~/screenshot.jpg"), "jpg")
    #print 'afer Selction'
    #myQTestWidget.show()
    #myQTestWidget.exec_()
    app.exec_()
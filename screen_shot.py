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
            self.rubberBand.hide()
            self.parent().selection = self.rubberBand.geometry()
            print self.parent().selection
            self.parent().close()


    def setTextLabelPosition (self, x, y):
        self.x, self.y = x, y
        self.setText('Please click on screen ( %d : %d )' % (self.x, self.y))





class SnapshotWidget (QtGui.QDialog):#QtGui.QDialog
    def __init__ (self, parent = None):
        super(SnapshotWidget, self).__init__(parent)

        self.selection = []
        self.setWindowOpacity(0.4)
        # Init QLabel
        self.positionQLabel = GetSelection(self)
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowState(QtCore.Qt.WindowFullScreen)
        #self.setWindowModality(QtCore.Qt.ApplicationModal)

        # Init QLayout
        layoutQHBoxLayout = QtGui.QHBoxLayout()
        layoutQHBoxLayout.addWidget(self.positionQLabel)
        self.setLayout(layoutQHBoxLayout)
        self.showFullScreen()

    def keyPressEvent(self, event):
        # Re-direct ESC key to closeEvent
        print(event)
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def show(self):
        print 'show me what you '

    def closeEvent(self, event):
        print "Closing main window"

        print 'by by tou beautifull World'
        print self.selection

    def __del__(self):
        pass
        #widgets = QtGui.QApplication.instance()
        #print widgets

    @staticmethod
    def get_data(parent=None):
        dialog = SnapshotWidget(parent)
        dialog.exec_()
        appInstance = QtCore.QCoreApplication.instance()
        screen = appInstance.desktop().winId()
        screenshot = QtGui.QPixmap.grabWindow(screen, dialog.selection.getRect())
        return screenshot


class TestSS(QtGui.QMainWindow):
    def __init__(self):
        super(TestSS,self).__init__()
        self.qlayout = QtGui.QHBoxLayout()
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
        self.button.setIconSize(QtCore.QSize(130, 130))
        self.button.setGeometry(QtCore.QRect(1030, 500, 161, 61))
        print  self.snapshot_widget,'ahha'




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
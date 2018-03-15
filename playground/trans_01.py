import sys
from PySide import QtGui, QtCore


class Selector(QtGui.QRubberBand):
    def __init__(self,*arg,**kwargs):
        super(Selector, self).__init__(*arg, **kwargs)

        self.setStyle(QtGui.QStyleFactory.create('windowsvista'))
        #self.palette = QtGui.QPalette(QtGui.QPalette.Active, QtGui.QPalette.Highlight, QtGui.QBrush(QtCore.Qt.green))


    def paintEvent(self, QPaintEvent):
        pass
        #find some way to Keep Rubberband Selection in All Os and styles the Same "perhaps Style Sheets "



class QCustomLabel (QtGui.QLabel):
    def __init__ (self, parent = None):
        super(QCustomLabel, self).__init__(parent)
        self.setMouseTracking(True)
        self.coloring = QtGui.QGraphicsColorizeEffect()
        self.rubberBand = Selector(QtGui.QRubberBand.Rectangle,self)
        self.origin = QtCore.QPoint()


    def mouseMoveEvent (self, eventQMouseEvent):
        #self.setTextLabelPosition(eventQMouseEvent.x(), eventQMouseEvent.y())
        #QtGui.QWidget.mouseMoveEvent(self, eventQMouseEvent)
        if not self.origin.isNull():
            self.rubberBand.setGeometry(QtCore.QRect(self.origin, eventQMouseEvent.pos()).normalized())

    def mousePressEvent (self, eventQMouseEvent):
        #if eventQMouseEvent.button() == QtCore.Qt.LeftButton:
            #QtGui.QMessageBox.information(self, 'Position', '( %d : %d )' % (self.x, self.y))
        #QtGui.QWidget.mousePressEvent(self, eventQMouseEvent)
        if eventQMouseEvent.button() == QtCore.Qt.LeftButton:
            self.origin = QtCore.QPoint(eventQMouseEvent.pos())
            self.rubberBand.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
            self.rubberBand.show()

    def mouseReleaseEvent(self, eventQMouseEvent):
        if eventQMouseEvent.button() == QtCore.Qt.LeftButton:
            self.rubberBand.hide()
            self.parent().selection = self.rubberBand.geometry()
            self.parent().close()

    def setTextLabelPosition (self, x, y):
        self.x, self.y = x, y
        self.setText('Please click on screen ( %d : %d )' % (self.x, self.y))





class QCustomWidget (QtGui.QWidget):
    def __init__ (self, parent = None):
        super(QCustomWidget, self).__init__(parent)
        self.selection = []
        self.setWindowOpacity(0.4)
        # Init QLabel
        self.positionQLabel = QCustomLabel(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

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


    def __del__(self):
        return self.selection
        print 'by by tou beautifull World'






myQApplication = QtGui.QApplication(sys.argv)
myQTestWidget = QCustomWidget()
myQTestWidget.show()
myQApplication.exec_()
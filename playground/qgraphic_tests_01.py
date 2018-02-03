import sys
from PySide.QtCore import *
from PySide.QtGui import *

class ImageView(QGraphicsView):
    def __init__(self, parent=None, origPixmap=None):
        """
        QGraphicsView that will show an image scaled to the current widget size
        using events
        """
        super(ImageView, self).__init__(parent)
        self.origPixmap = origPixmap
        QMetaObject.connectSlotsByName(self)

    def resizeEvent(self, event):
        """
        Handle the resize event.
        """
        size = event.size()
        item =  self.items()[0]

        # using current pixmap after n-resizes would get really blurry image
        #pixmap = item.pixmap()
        pixmap = self.origPixmap

        pixmap = pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.centerOn(1.0, 1.0)
        item.setPixmap(pixmap)


app = QApplication(sys.argv)

pic = QPixmap('pic.jpg')
grview = ImageView(origPixmap=pic)

scene = QGraphicsScene()
scene.addPixmap(pic)

grview.setScene(scene)
grview.show()

sys.exit(app.exec_())
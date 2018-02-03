import sys
from PySide import QtGui, QtCore

class MyDelegate(QtGui.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        mtview = QtGui.QTableView(parent)
        mtview.verticalHeader().setVisible(False)
        mtview.horizontalHeader().setVisible(False)
        mtmodel = QtGui.QStandardItemModel()
        mtview.setModel(mtmodel)
        return mtview

    def setEditorData(self, editor, modelindex):
        editor.resize(400,400)
        mtmodel = editor.model()
        for x in range(5):
            for y in range(5):
                mtmodel.setItem(x,y,QtGui.QStandardItem("%s, %s" % (x, y)))

class MyApp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setMinimumSize(200, 200)
        self.listview = QtGui.QListView()
        self.listview.setItemDelegate(MyDelegate())
        listmodel = QtGui.QStandardItemModel()

        self.setCentralWidget(self.listview)
        t = '123456789'
        for x in range(10):
            itemmodel=QtGui.QStandardItem(t)
            listmodel.appendRow(itemmodel)
        self.listview.setModel(listmodel)

def main():
    app = QtGui.QApplication(sys.argv)
    mw = MyApp()
    mw.show()
    app.exec_()

if __name__=="__main__":
    main()


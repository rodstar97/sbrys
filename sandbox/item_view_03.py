#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Custom QListView

This script demonstrates

 - DND item
 - sort item

Tested environment:
    Mac OS X 10.6.8

Docs

 - http://doc.qt.nokia.com/latest/model-view-programming.html#using-drag-and-drop-with-item-views

 - Qt - QAbstractItemView, PySide - QListView
 - Qt - QAbstractItemModel, PySide - QAbstractItemModel
"""
import glob
import os
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui

from component_widget import ComponentWidget


class ComponentDelegate(QtGui.QStyledItemDelegate):
    """
        Change Look from normal QListview item to custom Qwidget

    """
    def __init__(self, parent):
       QtGui.QStyledItemDelegate.__init__(self, parent)

    def getData(self, index):
        row = index.row()
        return self.components[row]

    def createEditor(self, parent, option, index):
        # Doubleclick Event
        editor = ComponentWidget(path=str(index.data()),parent = parent, selected=True)
        editor.setAutoFillBackground(True)
        return editor

    def flags(self, index):
        return QtGui.Qt.ItemIsEnabled | QtGui.Qt.ItemIsSelectable

    def paint(self, painter, option, index):
        componentWidget = ComponentWidget()#path=str(index.data())
        selectedComponetWidget = ComponentWidget( selected=True)#path=str(index.data()),
        painter.save()
        painter.translate(option.rect.topLeft())
        if option.state & QtGui.QStyle.State_Selected:
            selectedComponetWidget.resize(option.rect.size())
            selectedComponetWidget.render(painter, QtCore.QPoint())
            painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        else:
            componentWidget.resize(option.rect.size())
            componentWidget.render(painter, QtCore.QPoint())
            painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        painter.drawRect(option.rect)
        painter.restore()

    def sizeHint(self, options, index):
        return QtCore.QSize(100, 100)

class ListModel(QtCore.QAbstractListModel):
    def __init__(self, os_list):
        super(ListModel, self).__init__()
        self.os_list = os_list

    def rowCount(self, parent):
        return len(self.os_list)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        os_name, os_logo_path = self.os_list[index.row()]
        if role == QtCore.Qt.DisplayRole:
            return os_name
        elif role == QtCore.Qt.DecorationRole:
            return QtGui.QIcon(os_logo_path)

        return None

    def flags(self, idx):
        if idx.isValid():
            return QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled |\
                   QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        else:
            return QtCore.Qt.ItemIsDropEnabled |\
                   QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

    def supportedDropActions(self):
        return QtCore.Qt.MoveAction

    def mimeData(self, idxes):
        # NOTE: create mime data from ancestor method for fixed crash bug on PySide
        mime_data = super(ListModel, self).mimeData(idxes)

        encoded_data = ""

        for idx in idxes:
            if idx.isValid():
                encoded_data += '\r\n' + self.data(idx, role = QtCore.Qt.DisplayRole)

        mime_data.setData('text/plain', encoded_data)

        return mime_data



class ListView(QtGui.QListView):
    def __init__(self, parent=None):
        super(ListView, self).__init__(parent)

        self.data_sources = create_data_source()
        list_model = ListModel(self.data_sources)
        self.setModel(list_model)

        delegate = ComponentDelegate(self)
        self.setItemDelegate(delegate)

        # size
        self.setIconSize(QtCore.QSize(50, 50))
        self.setSpacing(5)
        self.setUniformItemSizes(True)
        self.setViewMode(QtGui.QListView.IconMode)
        self.setFlow(QtGui.QListView.LeftToRight)
        self.setWrapping(1)
        self.setResizeMode(QtGui.QListView.Adjust)

        # view
        self.setDropIndicatorShown(True)

        # interactive in DND mode
        #self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        #self.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        #self.setDragEnabled(True)
        #self.setAcceptDrops(True)

    def dropEvent(self, evt):
        mime_data = evt.mimeData()

        if mime_data.hasFormat('text/plain'):
            buf = mime_data.data('text/plain')
            print 'pos:', evt.pos()
            print "source == self:", evt.source() == self
            print 'mime data:', repr(buf)

        return super(ListView, self).dropEvent(evt)


def create_data_source1():
    logos = glob.glob('C:\Users\RF\Desktop\icons\*.png')
    return [(os.path.splitext(i)[0], i) for i in logos]

def create_data_source(filtername = ''):
    import sqlite3
    conn = sqlite3.connect('../tutorial.db')
    c = conn.cursor()
    c.execute("SELECT * FROM stuffToPlot WHERE keyword LIKE 'name%'")#'SELECT * FROM stuffToPlot WHERE value > 2'
    data = c.fetchall()
    #print(data)
    #for row in data:
        #print row[2]
    c.close
    conn.close()
    return data

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.layout = QtGui.QHBoxLayout()
        self.list_view = ListView(self)


        self.layout.addWidget(self.list_view)
        self.setLayout(self.layout)


        #x, y, w, h = 5, 5, 290, 250
        #self.list_view.setGeometry(x, y, w, h)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
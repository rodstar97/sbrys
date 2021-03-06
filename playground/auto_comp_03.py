import os
import sys
import json
from PySide import QtCore, QtGui


class LineEdit(QtGui.QLineEdit):
    def __init__(self, *args, **kwargs):
        QtGui.QLineEdit.__init__(self, *args, **kwargs)
        self.multipleCompleter = None

    def keyPressEvent(self, event):
        QtGui.QLineEdit.keyPressEvent(self, event)
        if not self.multipleCompleter:
            return
        c = self.multipleCompleter
        if self.text() == "":
            return
        c.setCompletionPrefix(self.cursorWord(self.text()))
        if len(c.completionPrefix()) < 1:
            c.popup().hide()
            return
        c.complete()

    def cursorWord(self, sentence):
        p = sentence.rfind(" ")
        if p == -1:
            return sentence
        return sentence[p + 1:]

    def insertCompletion(self, text):
        p = self.text().rfind(" ")
        if p == -1:
            self.setText(text)
        else:
            self.setText(self.text()[:p+1]+ text)

    def setMultipleCompleter(self, completer):
        self.multipleCompleter = completer
        self.multipleCompleter.setWidget(self)
        completer.activated.connect(self.insertCompletion)


def main():
    app = QtGui.QApplication(sys.argv)
    w = LineEdit()
    completer = QtGui.QCompleter(["Animals", "Dogs", "Birds", "Cats", "Elephant", "Zebra"])
    completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
    w.setMultipleCompleter(completer)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
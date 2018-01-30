from utils.convert_ui_files import convert
#from ui.qtd_main import Ui_sbrys_main_qw
from sbrysMainWidget import *
import os, sys
from PySide import QtGui,QtCore



'''Convert UI Files'''
pwd =os.path.dirname(os.path.realpath(__file__))
ui_files = os.path.join(pwd,'ui')
print ui_files
convert(ui_files)








app = QtGui.QApplication(sys.argv)
myWidget = MainWidget()
myWidget.show()
app.exec_()
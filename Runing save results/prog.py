from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_run
app = QtWidgets.QApplication(sys.argv)

run = QtWidgets.QDialog()
ui = Ui_run()
ui.setupUi(run)
run.show()

sys.exit(app.exec_())
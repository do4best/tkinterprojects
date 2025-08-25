from PyQt6 import QtWidgets,uic
import sys,os

app = QtWidgets.QApplication([])
win = uic.loadUi("c:/Users/RAVISCIENTIFIC/Desktop/player/python/log.ui")
win.show()
sys.exit(app.exec())
print(os.getcwd())
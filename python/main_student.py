import sys
from PyQt6.QtWidgets import QWidget,QApplication,QPushButton,QFrame,QMessageBox,QTableWidgetItem
from PyQt6.QtGui import QIntValidator
from student_ui import Ui_Form
from connect_database import ConnectDatabase

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
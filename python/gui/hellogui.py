import sys 
from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QTextEdit,QVBoxLayout
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello Qt6")
        self.resize(500,350)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.inputField = QLineEdit()
        button = QPushButton("&Say Hello",clicked=self.sayHello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText(f'Hello {inputText}')
        self.inputField = ""

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet('''
        QWidget{
                      font-size:25px;
                      }
        QPushButton{
                      font-size:20px
                      }
''')
    window = MyApp()
    window.show()
    app.exec()
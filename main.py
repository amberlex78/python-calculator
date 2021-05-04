from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("calculator.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# Your code here
form.label.setText("42")

app.exec_()

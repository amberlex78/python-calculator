from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("calculator.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# Fixed margin for label
form.label.setContentsMargins(10, 0, 10, 0)

app.exec_()

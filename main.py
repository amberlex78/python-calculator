from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("calculator.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# Fixed margin for label
form.lbl_display.setContentsMargins(10, 0, 10, 0)


def handler():
    form.btn_0.clicked.connect(lambda: add_number(form.btn_0.text()))
    form.btn_1.clicked.connect(lambda: add_number(form.btn_1.text()))
    form.btn_2.clicked.connect(lambda: add_number(form.btn_2.text()))
    form.btn_3.clicked.connect(lambda: add_number(form.btn_3.text()))
    form.btn_4.clicked.connect(lambda: add_number(form.btn_4.text()))
    form.btn_5.clicked.connect(lambda: add_number(form.btn_5.text()))
    form.btn_6.clicked.connect(lambda: add_number(form.btn_6.text()))
    form.btn_7.clicked.connect(lambda: add_number(form.btn_7.text()))
    form.btn_8.clicked.connect(lambda: add_number(form.btn_8.text()))
    form.btn_9.clicked.connect(lambda: add_number(form.btn_9.text()))

    form.btn_divide.clicked.connect(lambda: add_number(form.btn_divide.text()))
    form.btn_multiply.clicked.connect(lambda: add_number(form.btn_multiply.text()))
    form.btn_minus.clicked.connect(lambda: add_number(form.btn_minus.text()))
    form.btn_plus.clicked.connect(lambda: add_number(form.btn_plus.text()))

    form.btn_equal.clicked.connect(calc_result)
    form.btn_clear.clicked.connect(clear_lbl_display)


def add_number(number):
    if number == "x":
        number = "*"

    old_value = form.lbl_display.text()

    if old_value == "0":
        form.lbl_display.setText(number)
    else:
        form.lbl_display.setText(old_value + str(number))


def calc_result():
    res = eval(form.lbl_display.text())
    form.lbl_display.setText(str(res))


def clear_lbl_display():
    form.lbl_display.setText("0")


handler()
app.exec_()

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.passwd = None
        self.user_name = None
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./little_demo.ui")
        self.user_name = self.ui.lineEdit
        self.passwd = self.ui.lineEdit_2
        login_btn = self.ui.pushButton
        forget_btn = self.ui.pushButton_2
        # 事件绑定
        login_btn.clicked.connect(self.login)

    def login(self):
        print(self.user_name.text())
        print(self.passwd.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec_()
    
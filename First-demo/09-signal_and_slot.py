import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.text_browser = None
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
        self.text_browser = self.ui.textEdit
        # 事件绑定
        login_btn.clicked.connect(self.login)

    def login(self):
        user_name = self.user_name.text()
        passwd = self.passwd.text()
        if user_name == "admin" and passwd == "dp28ldp":
            self.text_browser.setText("欢迎%s" % user_name)
            self.text_browser.repaint()
        else:
            self.text_browser.setText("用户名或者密码错误...请重试")
            self.text_browser.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec_()
    
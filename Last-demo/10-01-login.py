import json
import sys
import time

import requests as requests
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget


class LoginThread(QThread):
    # 创建自定义信号
    start_login_signal = pyqtSignal(str)

    def __init__(self, signal):
        super(LoginThread, self).__init__()
        self.login_complete_signal = signal

    def login_by_requests(self, user_password_json):
        # 将json字符串，转换为自定，从而实现了传递用户名及密码
        user_password_json = json.loads(user_password_json)
        print(user_password_json.get("user_name"))
        print(user_password_json.get("passwd"))
        r = requests.post(url="https://service-afc54qrs-1253781421.gz.apigw.tencentcs.com/release/qt_login",
                          json=user_password_json)
        print("接收到腾讯云服务器的相应：", r.content.decode())
        ret = r.json()
        print("这里要发信号给UI线程")
        self.login_complete_signal.emit(json.dumps(ret))

    def run(self) -> None:
        # 通过while true的方式让子线程一直运行，而不是结束
        # 让子线程一直活着，从而有能力接收来自主线程（UI线程）的任务
        while True:
            print("子线程正在执行.....")
            time.sleep(1)


class MyWindow(QWidget):
    login_status_signal = pyqtSignal(str)

    def __init__(self):
        super(MyWindow, self).__init__()
        self.login_thread = None
        self.text_browser = None
        self.passwd = None
        self.user_name = None
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./little_demo.ui")
        # 提取要操作的控件
        self.user_name = self.ui.lineEdit
        self.passwd = self.ui.lineEdit_2
        login_btn = self.ui.pushButton
        forget_btn = self.ui.pushButton_2
        self.text_browser = self.ui.textBrowser
        # 绑定信号与槽函数
        login_btn.clicked.connect(self.login)

        # 创建一个信号，用来子线程登录成功之后，向主线程发送
        self.login_status_signal.connect(self.login_status)
        # 创建一个子线程（注意要将login_thread变量变为对象的属性，如果不是对象属性，而是普通的变量的话
        # 会随着init_ui函数执行结束而被释放，此时子线程还没有执行完毕，会产生问题
        self.login_thread = LoginThread(self.login_status_signal)
        # 将要创建的子线程类中的信号进行绑定
        self.login_thread.start_login_signal.connect(self.login_thread.login_by_requests)
        # 让子线程开始工作
        self.login_thread.start()

    def login(self):
        user_name = self.user_name.text()
        passwd = self.passwd.text()
        # 发送信号，让子线程开始登录
        self.login_thread.start_login_signal.emit(json.dumps({"user_name": user_name, "passwd": passwd}))

    def login_status(self, status):
        print("ststus...", status)
        status_dict = json.loads(status)
        print(status_dict.get("err_msg"))
        self.text_browser.setText(status_dict.get("err_msg"))
        self.text_browser.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec_()

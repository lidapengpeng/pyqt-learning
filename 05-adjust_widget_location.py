import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QDesktopWidget

if __name__ == '__main__':
    # part1: 创建应用
    app = QApplication(sys.argv)
    # part2: 窗体创建以及各控件内容
    w = QWidget()
    # 1、文本框
    text = QLabel("账号：", w)
    # 设置label的左上角位置x,y以及宽高w,h
    text.setGeometry(20, 20, 30, 20)
    # 2、输入框
    inputText = QLineEdit(w)
    inputText.setPlaceholderText("请输入账号")
    inputText.setGeometry(55, 20, 200, 20)
    # 3、按钮
    button = QPushButton("快戳我", w)
    button.setGeometry(50, 80, 70, 30)

    w.resize(300, 300)
    # 将窗口调整到屏幕中央
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(int(x - width/2), int(y - height/2))

    w.show()
    # part3:应用循环等待，持续检测
    app.exec_()

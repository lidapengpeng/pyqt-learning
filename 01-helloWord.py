import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # part1:创建一个事件检测对象，sys.argv相当于命令行输入的参数
    app = QApplication(sys.argv)
    # part2:窗体展示的内容
    # 创建界面对象
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle("第一个PyQT")
    # 显示窗口
    w.show()
    # part3:程序进入循环，等待检测
    app.exec_()


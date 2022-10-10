import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # sys.argv相当于命令行输入的参数
    app = QApplication(sys.argv)
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle("第一个PyQT")
    # 显示窗口
    w.show()
    # 程序进入循环等待
    app.exec_()


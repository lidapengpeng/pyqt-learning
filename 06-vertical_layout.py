import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        # 切记一定要调用父类的__init__()初始化方法,先让父类的初始化方法调用
        super(MyWindow, self).__init__()
        # 设置窗口大小
        self.resize(300, 300)
        # 设置窗口标题
        self.setWindowTitle("一个很厉害的程序")
        # 创建一个布局器，对窗体控件布局进行一种约束
        layout = QVBoxLayout()
        # 创建三个按钮，并将按钮添加到布局控件
        btn1 = QPushButton("老大叫大郎")
        layout.addWidget(btn1)
        btn2 = QPushButton("老二叫二郎")
        layout.addWidget(btn2)
        btn3 = QPushButton("老三叫李狗蛋")
        layout.addWidget(btn3)
        # stretch加一个伸缩的对象（理解为一个弹簧），
        # 参数1指的是，上面的空和下面的空1：1，参数2值得是上面的空和下面的空1：2
        # layout.addStretch(2)
        # 让当前的窗口按照这个规则排列
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedLayout, QLabel


class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        QLabel("我是窗体1要现实的内容", self)
        self.setStyleSheet("background-color:red;")


class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        QLabel("我是窗体2要现实的内容", self)
        self.setStyleSheet("background-color:green;")


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.stacked_layout = None
        self.show_window_layout()
        self.init_ui()

    def show_window_layout(self):
        # 创建堆叠（抽屉）布局
        self.stacked_layout = QStackedLayout()
        # 创建两个窗口（抽屉）
        win1 = Window1()
        win2 = Window2()
        # 将创建的两个窗口控件添加到堆叠（抽屉）布局中
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        # 设置widget大小以及固定宽高
        self.setFixedSize(300, 270)
        # 1、创建一个整体的布局器
        container = QVBoxLayout()

        # 2、创建一个具体要显示的子窗体
        show_window = QWidget()
        # 抽屉布局
        show_window.setLayout(self.stacked_layout)
        show_window.setStyleSheet("background-color:grey;")

        # 3、创建两个按钮控件
        btn1 = QPushButton("按钮1")
        btn2 = QPushButton("按钮2")
        # 给按钮添加事件
        btn1.clicked.connect(self.click_btn1)
        btn2.clicked.connect(self.click_btn2)

        # 4、添加控件到布局器
        container.addWidget(show_window)
        container.addWidget(btn1)
        container.addWidget(btn2)
        # 5、确定整体窗体的布局规则
        self.setLayout(container)

    def click_btn1(self):
        # 设置抽屉布局器的当前索引值，即可显示哪个widget
        self.stacked_layout.setCurrentIndex(0)

    def click_btn2(self):
        self.stacked_layout.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

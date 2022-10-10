import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 300)
        self.setWindowTitle("这是一个神奇的程序")
        # 设置垂直布局
        container = QVBoxLayout()

        # part1:创建爱好组
        hobby_box = QGroupBox("爱好")
        # 设置这个组内的控件布局为垂直排列
        v_layout = QVBoxLayout()
        btn1 = QRadioButton("吸烟")
        btn2 = QRadioButton("喝酒")
        btn3 = QRadioButton("打牌")
        # 将按钮控件添加到垂直布局中
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        # 将v_layout规则添加到hobby_box中
        hobby_box.setLayout(v_layout)

        # part2:创建性别组
        gender_box = QGroupBox("性别")
        # 设置这个组内的空间布局为水平排列
        h_layout = QHBoxLayout()
        btn4 = QRadioButton("男")
        btn5 = QRadioButton("女")
        # 将按钮控件添加至水平布局中
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        # 将h_layout添加到gender_box组中
        gender_box.setLayout(h_layout)

        # part3:将爱好组和性别组添加至全局布局中
        container.addWidget(hobby_box)
        container.addWidget(gender_box)

        # 设置全局布局规则
        self.setLayout(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

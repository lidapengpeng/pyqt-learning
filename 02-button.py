import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

if __name__ == '__main__':
    # part1:开启一个新的应用
    app = QApplication(sys.argv)
    # part2:应用窗体和相关事件
    w = QWidget()
    w.setWindowTitle("按钮测试")
    # 设置按钮
    button = QPushButton("点我")
    # 设置按钮的父窗口，为了让它与窗口一起显示
    button.setParent(w)
    # 窗体的显示
    w.show()
    # part3: 应用持续进行事件检测
    app.exec_()


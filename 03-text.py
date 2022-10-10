import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    text = QLabel("我爱你", w)
    # 设置label的左上角位置x,y以及宽高w,h
    text.setGeometry(20, 20, 100, 100)
    w.show()
    app.exec_()

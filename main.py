import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口的标题和大小
        self.setWindowTitle('PyQt5 Demo')
        self.setGeometry(100, 100, 300, 200)
        # 设置背景颜色
        

        # 创建一个按钮，设置文本和按钮点击事件
        btn = QPushButton('Click Me', self)
        btn.setGeometry(100, 70, 100, 40)
        btn.clicked.connect(self.showMessage)

    def showMessage(self):
        # 弹出一个消息框
        QMessageBox.information(self, 'Message', 'Hello, PyQt5!', QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

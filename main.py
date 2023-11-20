from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QColor, QPolygon
import sys
import random

SCREEN_SIZE = [680, 480]


class Solve(QMainWindow):
    def __init__(self):
        super().__init__()
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # random color
        # self.color = (255, 255, 0)  # yellow
        # uic.loadUi("UI.ui", self)
        
        self.flag = False
        self.setWindowTitle('Git')
        self.pushButton.setText('Нажми меня')
        self.pushButton.clicked.connect(self.draw)
        self.coords = []

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.size = random.randint(10, 100)
            self.x, self.y = random.randint(100, SCREEN_SIZE[0] - 100), random.randint(100, SCREEN_SIZE[1] - 100)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Solve()
    ex.show()
    sys.exit(app.exec_())

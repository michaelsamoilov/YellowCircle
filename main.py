import sys
from random import randint

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circles = []
        self.pushButton.clicked.connect(self.add)

    def add(self):
        r = randint(10, 50)
        x = randint(50, 550)
        y = randint(50, 550)
        rr = randint(0, 255)
        gg = randint(0, 255)
        bb = randint(0, 255)
        self.circles.append((x, y, r, rr, gg, bb))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def draw_circles(self, qp):
        for x, y, r, rr, gg, bb in self.circles:
            qp.setBrush(QColor(rr, gg, bb))
            qp.drawEllipse(QPoint(x, y), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

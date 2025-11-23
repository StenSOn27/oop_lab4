from PyQt6.QtGui import QPainter
from .shape import Shape
from PyQt6.QtCore import Qt

class PointShape(Shape):
    def draw(self, painter: QPainter, filled=True):
        painter.setPen(Qt.GlobalColor.black)
        painter.drawPoint(int(self.x1), int(self.y1))

from PyQt6.QtGui import QPainter
from .shape import Shape
from PyQt6.QtCore import Qt

class LineShape(Shape):
    def draw(self, painter: QPainter, filled=True):
        painter.setPen(Qt.GlobalColor.black)
        painter.drawLine(int(self.x1), int(self.y1), int(self.x2), int(self.y2))

from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt
from .shape import Shape

class EllipseShape(Shape):
    def draw(self, painter, filled=True):
        cx, cy = self.x1, self.y1
        ex, ey = self.x2, self.y2
        rx = abs(ex - cx)
        ry = abs(ey - cy)

        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.BrushStyle.NoBrush)

        painter.drawEllipse(cx - rx, cy - ry, rx * 2, ry * 2)

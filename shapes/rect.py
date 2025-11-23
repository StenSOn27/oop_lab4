from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import Qt
from .shape import Shape

class RectShape(Shape):
    def draw(self, painter, filled=True):
        x = min(self.x1, self.x2)
        y = min(self.y1, self.y2)
        w = abs(self.x2 - self.x1)
        h = abs(self.y2 - self.y1)

        if filled:
            painter.setBrush(QBrush(QColor("lightblue")))
        else:
            painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawRect(x, y, w, h)

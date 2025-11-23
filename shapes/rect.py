from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import Qt
from .shape import Shape

class RectShape(Shape):
    def draw(self, painter, filled=True):
        if filled:
            brush_color = "lightblue"
        else:
            brush_color = None

        x = min(self.x1, self.x2)
        y = min(self.y1, self.y2)
        w = abs(self.x2 - self.x1)
        h = abs(self.y2 - self.y1)

        painter.setPen(Qt.GlobalColor.black)
        if brush_color:
            painter.setBrush(QBrush(QColor(brush_color)))
        else:
            painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawRect(x, y, w, h)

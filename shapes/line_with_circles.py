from PyQt6.QtGui import QPen
from PyQt6.QtCore import Qt
from shapes import LineShape, EllipseShape

class LineWithCircles(LineShape, EllipseShape):
    def draw(self, painter, filled=True):
        LineShape.draw(self, painter, filled=True)

        r = 6
        cx1, cy1 = self.x1, self.y1
        cx2, cy2 = self.x2, self.y2

        painter.setPen(Qt.GlobalColor.red)

        self.x1, self.y1 = cx1, cy1
        self.x2, self.y2 = cx1 + r, cy1 + r
        EllipseShape.draw(self, painter, filled=False)

        self.x1, self.y1 = cx2, cy2
        self.x2, self.y2 = cx2 + r, cy2 + r
        EllipseShape.draw(self, painter, filled=False)

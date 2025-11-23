from PyQt6.QtGui import QPen
from PyQt6.QtCore import Qt
from shapes import LineShape, EllipseShape


class LineOOShape(LineShape, EllipseShape):
    def draw(self, painter, filled=True):
        LineShape.draw(self, painter, filled)
        r = 6

        ox1, oy1, ox2, oy2 = self.x1, self.y1, self.x2, self.y2

        self.x1 = int(ox1 - r // 2)
        self.y1 = int(oy1 - r // 2)
        self.x2 = int(ox1 + r // 2)
        self.y2 = int(oy1 + r // 2)
        EllipseShape.draw(self, painter, filled=True)

        self.x1 = int(ox2 - r // 2)
        self.y1 = int(oy2 - r // 2)
        self.x2 = int(ox2 + r // 2)
        self.y2 = int(oy2 + r // 2)
        EllipseShape.draw(self, painter, filled=True)

        self.x1, self.y1, self.x2, self.y2 = ox1, oy1, ox2, oy2

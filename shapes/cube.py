from shapes import RectShape, LineShape
from PyQt6.QtCore import Qt
from shape_factory import make_shape

class CubeFrame(RectShape, LineShape):
    def draw(self, painter, filled=True):
        x1, y1 = self.x1, self.y1
        x2, y2 = self.x2, self.y2

        w = abs(x2 - x1)
        h = abs(y2 - y1)

        dx = w * 0.3
        dy = h * 0.3

        RectShape.draw(self, painter)

        rear = make_shape("rect")
        rear.x1 = x1 + dx
        rear.y1 = y1 + dy
        rear.x2 = x2 + dx
        rear.y2 = y2 + dy
        rear.draw(painter)

        pairs = [
            (x1, y1, x1 + dx, y1 + dy),
            (x2, y1, x2 + dx, y1 + dy),
            (x1, y2, x1 + dx, y2 + dy),
            (x2, y2, x2 + dx, y2 + dy),
        ]

        for sx, sy, ex, ey in pairs:
            line = make_shape("line")
            line.x1, line.y1 = sx, sy
            line.x2, line.y2 = ex, ey
            line.draw(painter)
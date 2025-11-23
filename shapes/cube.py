from shapes import RectShape, LineShape
from PyQt6.QtCore import Qt

class CubeFrame(RectShape, LineShape):
    def draw(self, painter, filled=True):
        x1, y1 = self.x1, self.y1
        x2, y2 = self.x2, self.y2

        w = abs(x2 - x1)
        h = abs(y2 - y1)

        dx = int(w * 0.3)
        dy = int(h * 0.3)

        original_coords = (self.x1, self.y1, self.x2, self.y2)
        self.x1, self.y1 = x1 + dx, y1 + dy
        self.x2, self.y2 = x2 + dx, y2 + dy
        painter.setPen(Qt.GlobalColor.black)
        super().draw(painter, filled=False)

        self.x1, self.y1, self.x2, self.y2 = original_coords

        pairs = [
            (x1, y1, x1 + dx, y1 + dy),
            (x2, y1, x2 + dx, y1 + dy),
            (x1, y2, x1 + dx, y2 + dy),
            (x2, y2, x2 + dx, y2 + dy),
        ]

        for sx, sy, ex, ey in pairs:
            original_line_coords = (self.x1, self.y1, self.x2, self.y2)
            self.x1, self.y1, self.x2, self.y2 = sx, sy, ex, ey
            LineShape.draw(self, painter, filled)
            self.x1, self.y1, self.x2, self.y2 = original_line_coords

        super().draw(painter, filled=False)

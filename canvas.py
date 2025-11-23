from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt
from shape_factory import make_shape

class Canvas(QWidget):
    def __init__(self, parent=None, max_shapes=132):
        super().__init__(parent)
        self.N = max_shapes
        self.pcshape = [None] * self.N
        self.obj_count = 0

        self.current_type = None
        self.temp_shape = None
        self.drawing = False

    def set_shape_type(self, t):
        self.current_type = t

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton and self.current_type:
            self.drawing = True
            self.temp_shape = make_shape(self.current_type)
            self.temp_shape.set_start(e.position().x(), e.position().y())
            self.temp_shape.set_end(e.position().x(), e.position().y())

    def mouseMoveEvent(self, e):
        if self.drawing:
            self.temp_shape.set_end(e.position().x(), e.position().y())
            self.update()

    def mouseReleaseEvent(self, e):
        if self.drawing:
            self.temp_shape.set_end(e.position().x(), e.position().y())
            self.pcshape[self.obj_count] = self.temp_shape
            self.obj_count += 1
            self.temp_shape = None
            self.drawing = False
            self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        for i in range(self.obj_count):
            shape = self.pcshape[i]
            if shape is not None:
                shape.draw(p, filled=True)

        if self.temp_shape is not None:
            p.setPen(QPen(Qt.GlobalColor.black, 1))
            self.temp_shape.draw(p, filled=False)

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.x1 = self.y1 = 0
        self.x2 = self.y2 = 0

    def set_start(self, x, y):
        self.x1 = int(x)
        self.y1 = int(y)

    def set_end(self, x, y):
        self.x2 = int(x)
        self.y2 = int(y)

    @abstractmethod
    def draw(self, painter, filled=True):
        pass

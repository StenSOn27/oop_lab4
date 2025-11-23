from shapes.point import PointShape
from shapes.line import LineShape
from shapes.rect import RectShape
from shapes.ellipse import EllipseShape
from shapes.line_with_circles import LineWithCircles
from shapes.cube_frame import CubeFrame

SHAPE_CLASSES = {
    "point": PointShape,
    "line": LineShape,
    "rect": RectShape,
    "ellipse": EllipseShape,
    "linecirc": LineWithCircles,
    "cube": CubeFrame,
}

def make_shape(shape_type: str):
    cls = SHAPE_CLASSES.get(shape_type)
    return cls() if cls else None

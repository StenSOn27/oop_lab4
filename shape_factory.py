import importlib

SHAPE_CLASSES = {
    "point": "shapes.point.PointShape",
    "line": "shapes.line.LineShape",
    "rect": "shapes.rect.RectShape",
    "ellipse": "shapes.ellipse.EllipseShape",
    "linecirc": "shapes.line_with_circles.LineOOShape",
    "cube": "shapes.cube.CubeFrame",
}

def make_shape(shape_type: str):
    path = SHAPE_CLASSES.get(shape_type)
    if not path:
        return None

    module_name, class_name = path.rsplit(".", 1)

    module = importlib.import_module(module_name)
    cls = getattr(module, class_name)

    return cls()

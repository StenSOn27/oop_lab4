from PyQt6.QtWidgets import QMainWindow, QToolBar
from PyQt6.QtGui import QIcon, QAction
from canvas import Canvas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lab 3")
        self.setFixedSize(1000, 800)

        self.canvas = Canvas(self)
        self.setCentralWidget(self.canvas)

        self.actions = {}
        self.init_ui()

    def init_ui(self):
        self.create_toolbar()
        self.create_menu()

    def create_toolbar(self):
        self.toolbar = QToolBar("Shapes")
        self.addToolBar(self.toolbar)

        self.add_button("point", "icons/point", "Створити точку")
        self.add_button("line", "icons/line", "Створити лінію")
        self.add_button("rect", "icons/rectangle", "Створити прямокутник")
        self.add_button("ellipse", "icons/ellipse", "Створити еліпс")

    def add_button(self, name: str, icon_file: str, tip: str):
        act = QAction(QIcon(f"{icon_file}.png"), "", self)
        act.setToolTip(tip)
        act.setCheckable(True)
        act.triggered.connect(lambda _, n=name: self.set_shape(n))
        self.actions[name] = act
        self.toolbar.addAction(act)

    def create_menu(self):
        menubar = self.menuBar()
        menubar.addMenu("Файл")
        obj_menu = menubar.addMenu("Об’єкти")
        menubar.addMenu("Довідка")

        for act in self.actions.values():
            obj_menu.addAction(act)

        obj_menu.aboutToShow.connect(self.update_menu_checks)

    def update_menu_checks(self):
        for name, act in self.actions.items():
            act.setChecked(name == self.canvas.current_type if self.canvas.current_type else False)

    def set_shape(self, name):
        self.canvas.set_shape_type(name)
        for n, act in self.actions.items():
            act.setChecked(n == name)

        self.setWindowTitle(f"Lab 3 — Поточний об’єкт: {name}")
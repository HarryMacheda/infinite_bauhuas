from abc import ABC, abstractmethod

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

class Shape(ABC):
    def __init__(self, position:Position, fill="white", stroke="black"):
        self.fill = fill
        self.stroke = stroke
        self.position = position

    @abstractmethod
    def draw_tk(self, canvas):
        """Draw shape on a Tkinter canvas."""
        pass

    @abstractmethod
    def draw_svg(self, dwg):
        """Add shape to an svgwrite.Drawing object."""
        pass
    
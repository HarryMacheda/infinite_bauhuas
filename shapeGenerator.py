import random
from shapes.circle import Circle
from shapes.line import Line
from shapes.shape import Position, Shape
from shapes.square import Square

PADDING = 50

class ShapeGenerator:
    def __init__(self, canvas_width=300, canvas_height=200):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        
    def get_shape(self) -> 'Shape':
        shape_type = random.choice(['circle', 'square'])

        fill = random.choice(["red", "blue", "yellow"])

        if shape_type == 'circle':
            r = random.randint(10, 50)
            cx = random.randint(PADDING, self.canvas_width - PADDING)
            cy = random.randint(PADDING, self.canvas_height - PADDING)
            return Circle(Position(cx, cy), r, fill=fill, stroke=fill)

        elif shape_type == 'square':
            size = random.randint(20, 80)
            x = random.randint(PADDING, self.canvas_width - PADDING)
            y = random.randint(PADDING, self.canvas_height - PADDING)
            return Square(Position(x, y), size, fill=fill, stroke=fill)     
    
    def get_line(self) -> 'Line':
        x1 = random.randint(PADDING, self.canvas_width - PADDING)
        y1 = random.randint(PADDING, self.canvas_height - PADDING)
        x2 = random.randint(PADDING, self.canvas_width - PADDING)
        y2 = random.randint(PADDING, self.canvas_height - PADDING)
        width = random.randint(1, 5)
        return Line(Position(x1, y1), Position(x2, y2), width=width)           

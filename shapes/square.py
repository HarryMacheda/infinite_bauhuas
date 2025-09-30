from shapes.shape import Position, Shape

class Square(Shape):
    def __init__(self, position:Position, size, fill="white", stroke="black"):
        super().__init__(position, fill, stroke)
        self.size = size

    def draw_tk(self, canvas):
        x0 = self.position.x
        y0 = self.position.y
        x1 = self.position.x + self.size
        y1 = self.position.y + self.size
        canvas.create_rectangle(x0, y0, x1, y1, fill=self.fill, outline=self.stroke)

    def draw_svg(self, dwg):
        dwg.add(dwg.rect(insert=(self.position.x, self.position.y),
                         size=(self.size, self.size),
                         fill=self.fill,
                         stroke=self.stroke))
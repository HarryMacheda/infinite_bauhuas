from shapes.shape import Position, Shape


class Line(Shape):
    def __init__(self, start:Position, end:Position, width=2, fill="black"):
        super().__init__(start, fill, stroke=fill)
        self.x1 = start.x
        self.y1 = start.y
        self.x2 = end.x
        self.y2 = end.y
        self.width = width

    def draw_tk(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2,
                           fill=self.fill, width=self.width)
        print(self.fill)

    def draw_svg(self, dwg):
        dwg.add(dwg.line(start=(self.x1, self.y1),
                         end=(self.x2, self.y2),
                         stroke=self.fill,
                         stroke_width=self.width))

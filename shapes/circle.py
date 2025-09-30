from shapes.shape import Position, Shape


class Circle(Shape):
    def __init__(self, position:Position, r, fill="white", stroke="black"):
        super().__init__(position, fill, stroke)
        self.r = r

    def draw_tk(self, canvas):
        x0 = self.position.x - self.r
        y0 = self.position.y - self.r
        x1 = self.position.x + self.r
        y1 = self.position.y + self.r
        canvas.create_oval(x0, y0, x1, y1, fill=self.fill, outline=self.stroke)

    def draw_svg(self, dwg):
        dwg.add(dwg.circle(center=(self.position.x, self.position.y),
                           r=self.r,
                           fill=self.fill,
                           stroke=self.stroke))
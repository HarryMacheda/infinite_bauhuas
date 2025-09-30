from shapeGenerator import ShapeGenerator


generator = ShapeGenerator(canvas_width=300, canvas_height=200)

shapes = [generator.get_shape() for _ in range(3)]
lines = [generator.get_line() for _ in range(2)]

# Tkinter Display
import tkinter as tk
import svgwrite

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

for shape in shapes + lines:
    shape.draw_tk(canvas)

# SVG Save
dwg = svgwrite.Drawing("random_shapes.svg", size=(300, 200))
for shape in shapes + lines:
    shape.draw_svg(dwg)
dwg.save()

root.mainloop()
print("Random SVG saved to random_shapes.svg")

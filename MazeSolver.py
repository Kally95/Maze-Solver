from tkinter import Tk, BOTH, Canvas
from Point import Line, Point
class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("My Window")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        
    def close(self):
        self.running = False
        self.root.destroy()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
    
def main():
    win = Window(800, 600)
    p1 = Point(1, 1)
    p2 = Point(100, 100)
    line = Line(p1, p2)
    win.draw_line(line, "black")
    win.wait_for_close() 

if __name__ == "__main__":
    main()
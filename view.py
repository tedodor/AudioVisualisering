import tkinter as tk, random

WINDOW_SIZE = (500,500)
CIRCLE_SIZE = 10
CURSOR_SIZE = 50

class View:
    def __init__(self, threshold):
        self.root = tk.Tk()
        self.thresh = threshold
        self.w = tk.Canvas(self.root, width=WINDOW_SIZE[0], height=WINDOW_SIZE[1])
        self.w.create_rectangle(0, 0, 1000, 1000, fill="white")
        self.w.pack()
        self.x = 0
        self.y = 0
        self.cursor = self.w.create_oval(self.x-threshold,self.y-threshold,self.x+threshold,self.y+threshold,outline="red")
        self.root.bind("<Motion>", self.motion)
        
    def draw_circle(self, x, y):
        self.w.create_oval(x,y,x+CIRCLE_SIZE,y+CIRCLE_SIZE,outline="blue",fill="blue")

    def draw(self,points):
        for p in points:
            self.draw_circle(p.x,p.y)

    def get_mouse_pos(self):
        return (self.x, self.y)

    def motion(self, event):
        print(event.x, event.y)
        self.w.move(self.cursor, event.x - self.x , event.y - self.y)
        self.x, self.y = event.x, event.y


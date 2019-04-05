import tkinter as tk, random

WINDOW_SIZE = (500,500)
CIRCLE_SIZE = 10
CURSOR_SIZE = 50
root = tk.Tk()

class View:
    def __init__(self, threshold):
        
        self.thresh = threshold
        self.w = tk.Canvas(root, width=WINDOW_SIZE[0], height=WINDOW_SIZE[1])
        self.w.create_rectangle(0, 0, WINDOW_SIZE[0]*2, WINDOW_SIZE[1]*2, fill="white")
        self.w.pack()
        self.x = 0
        self.y = 0
        self.cursor = self.w.create_oval(self.x-threshold,self.y-threshold,self.x+threshold,self.y+threshold,outline="red")
        root.bind("<Motion>", self.motion)
        #        self.root.bind("<MouseWheel>", self.scroll)
        
    def draw_circle(self, x, y):
        self.w.create_oval(x,y,x+CIRCLE_SIZE,y+CIRCLE_SIZE,outline="blue",fill="blue")

    def draw(self,points):
        print("drawing {} points".format(len(points)))
        for p in points:
            self.draw_circle(p.x,p.y)

    def get_mouse_pos(self):
        return (self.x, self.y)

    def motion(self, event):
        self.w.move(self.cursor, event.x - self.x , event.y - self.y)
        self.x, self.y = event.x, event.y


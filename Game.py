from tkinter import *
import random
import time
class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        s=[-3, -2, 2, 3]
        self.x = random.choice(s)
        self.y = random.choice(s)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(200,200, text='GaMe OvEr',font=('B nazanin',40),fill='red')
        if self.hit_paddle(pos) == True:
                self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >=self.canvas_width:
            self.x = -3
        
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        canvas.bind_all('<KeyPress-Right>', self.turn_right)
        canvas.bind_all('<KeyPress-Left>', self.turn_left)
    def turn_left(self, evt):
        self.x = -4
    def turn_right(self, evt):
        self.x=4


    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos=self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

                    
tk = Tk()
tk.title("GaMe")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=400, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
P1 = Paddle(canvas,'blue')
b1 = Ball(canvas,'brown', P1)
while 1:
    if b1.hit_bottom == False:
        b1.draw()
        P1.draw()
        
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    

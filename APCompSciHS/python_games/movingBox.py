from tkinter import *
import time, random
tk = Tk()
canvas = Canvas(tk, width = 1000, height = 1000)
canvas.pack()
def move(event):
    if event.keysym == 'Up':
        global y
        global y1
        y-=10
        y1-=10
    elif event.keysym == 'Down':      
        y+=10
        y1+=10
    elif event.keysym == 'Right':
        global x
        global x1
        x+=10
        x1+=10
    elif event.keysym == 'Left':
        x-=10
        x1-=10


background = canvas.create_rectangle(0, 0, 1000, 1000, fill = 'orange') #draws background
ranNum=random.random()*960  #Creates a random number
ranNum1=random.random()*960 #Creates a random number
r1 = None
o = 0
length = 4
x = 500
y = 500
x1 = 515
y1 = 515
while o < length:          
    r=canvas.create_rectangle(x, y, x1, y1, fill = 'blue')
    tk.bind('<KeyPress-Up>', move )
    tk.bind('<KeyPress-Down>', move)
    tk.bind('<KeyPress-Left>', move)
    tk.bind('<KeyPress-Right>', move)
    time.sleep(.01)
    canvas.delete(r1)
    r1 = r
    tk.update()
    tk.update_idletasks()

tk.mainloop()
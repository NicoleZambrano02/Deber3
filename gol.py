
import time
from tkinter import *
from tkinter import messagebox

tk=Tk()
x=0
y=0
canvas=Canvas(tk,width=450,height=326)
canvas.pack()


stadium=PhotoImage(file='stadium.gif')
ball=PhotoImage(file='ball.gif')


canvas.create_image(0,0,anchor=NW,image=stadium)
canvas.create_image(211,150,anchor=NW,image=ball)

def moveball(event):
    global x,y
    
    if event.keysym=='Up':
        canvas.move(2, 0, -3)
        y=y-3
    elif event.keysym=='Down':
        canvas.move(2,0,3)
        y=y+3
    elif event.keysym=='Left':
        canvas.move(2,-3,0)
        x=x-3
    else:
        canvas.move(2,3,0)
        x=x+3
        
    if x==180 or x==-183:
        messagebox.showinfo(message="GOOOOAL",title="MENSAJE")

    
       
canvas.bind_all('<KeyPress-Up>', moveball)
canvas.bind_all('<KeyPress-Down>', moveball)
canvas.bind_all('<KeyPress-Left>', moveball)
canvas.bind_all('<KeyPress-Right>', moveball)
tk.mainloop()

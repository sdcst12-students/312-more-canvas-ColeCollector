#!python3

# Find an image to use as a sprite from the Internet.
# Modify the image (flipping horizontally is a quick way to do that) so that you have
# a second, different image. Use the tkObject.after() method to animate it.
# Note: You can find sprite sheets or tile sheets on the internet to help you!

import tkinter as tk

w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()

walls = []
rec = c.create_rectangle(50,50,80,80,fill="#aa0000")



def keyPress(e):

    if e.keysym == "Up":
        x=0
        y=-5
        c.move(rec,x,y)

    elif e.keysym == "Right":
        x=5
        y=0
        c.move(rec,x,y)    

    elif e.keysym == "Down":
        x=0
        y=5
        c.move(rec,x,y)

    elif e.keysym == "Left":
        x=-5
        y=0
        c.move(rec,x,y) 
    
w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)


w.mainloop()
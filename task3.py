#!python3

# Find an image to use as a sprite from the Internet.
# Modify the image (flipping horizontally is a quick way to do that) so that you have
# a second, different image. Use the tkObject.after() method to animate it.
# Note: You can find sprite sheets or tile sheets on the internet to help you!

import tkinter as tk
from PIL import ImageTk,Image
import random
import time

w = tk.Tk()
w.attributes("-topmost",True)
w.geometry("500x250")
w.title("sample")
tile = 0
x = 0
y = 0
a = 0

c = tk.Canvas(w,width=475,height=280)
c.pack()

images = []

img = Image.open("assets/spritesheet.png").convert("RGBA")


for i in range(0,16):
    image = ImageTk.PhotoImage( img.crop([x,y,x+64,y+64]))
    x += 64
    if x == 256 and y == 0:
        x = 0
        y = 64

    elif x == 256 and y == 64:
        x = 0
        y = 128

    elif x == 256 and y == 128:
        x = 0
        y = 192

    images.append(image)


rec = c.create_image(64,64,image=images[0])

def update():
    global tile 
    ig = None
    tile = tile + 1
    tile = tile%4
    if tile == 0: 
        ig = images[a]

    elif tile == 1:
        ig = images[a+1]

    elif tile == 2:
        ig = images[a+2]

    elif tile == 3:
        ig = images[a+3]



    c.itemconfig(rec,image=ig)
    w.after(200,update)


def keyPress(e):
    global a

    if e.keysym == "Up":
        x=0
        y=-5
        c.move(rec,x,y)
        a = 12

    elif e.keysym == "Right":
        x=5
        y=0
        c.move(rec,x,y)
        a = 8

    elif e.keysym == "Down":
        x=0
        y=5
        c.move(rec,x,y)
        a = 0

    elif e.keysym == "Left":
        x=-5
        y=0
        c.move(rec,x,y) 
        a = 4
    
w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)


w.after(200,update)

w.mainloop()
#!python3

# Adding an image that is constantly changing using the tk.after() command

import tkinter as tk
from PIL import ImageTk,Image
import random
import time

#tile = 0

#def update():
    # alternates the tile between state 0 and 1 using modulus
    # depending on the state, the image contents are changed and 
    # a new timer is set to change again in 200 milliseconds
    #global tile
    #ig = None
    #tile +=1
    #tile = tile%2
    #if tile: 
    #    ig = img
    #else: 
    #   ig = img2

    #c.itemconfig(wim,image=ig)
    #w.after(200,update)

w = tk.Tk()
w.attributes("-topmost",True)
w.geometry("500x250")
tile = 0


c = tk.Canvas(w,width=475,height=280)
c.pack()
img = Image.open("assets/spritesheet.png").convert("RGBA")
img1 = ImageTk.PhotoImage( img.crop([0,0,64,64]))
img2 = ImageTk.PhotoImage( img.crop([64,0,128,64]))
img3 = ImageTk.PhotoImage( img.crop([192,0,256,64]))

rec = c.create_image(64,64,image=img3)

def update():
    global tile 
    ig = None
    tile = tile + 1
    tile = tile%3
    if tile == 0: 
        ig = img1
    elif tile == 1:
        ig = img2
    elif tile == 2:
        ig = img3


    c.itemconfig(rec,image=ig)
    print(tile)
    w.after(200,update)


w.after(200,update)


w.mainloop()
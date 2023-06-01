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

c = tk.Canvas(w,width=475,height=280)
c.pack()
img = Image.open("assets/spritesheet.png")
img2 = img.crop([0,0,64,64])

rec = c.create_image(0,0,image=img2)



#w.after(200,update)


w.mainloop()
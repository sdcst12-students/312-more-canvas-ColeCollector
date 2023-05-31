import tkinter as tk
import random

"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountains
5 Swamp
6 City
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()

rec = c.create_rectangle(5,35,25,55,fill="#aa0000")
walls = []

f = open('map1.txt','r')


x=0
Walls = []

while True:
    Walls.append(f.readline())
    x = x+1
    if x>15:
        break


for i in range(len(Walls)):
    for j in range(len(Walls[i])):
        if Walls[i][j] == "0":
        elif Walls[i][j] == "1":
        elif Walls[i][j] == "2":
        elif Walls[i][j] == "3":
        elif Walls[i][j] == "4":
        elif Walls[i][j] == "5":



def detectCollision():
    collisions = 0
    br = c.bbox(rec)

    for i in walls:
        if (i[0] <= (br[0] + xx ) <=i[2] or i[0] <= (br[2] + xx) <=i[2]) and (i[1] <= (br[1] + yy) <= i[3] or i[1] <= (br[3] + yy) <= i[3]):
            collisions = collisions+1

    if collisions > 0:
        return True
    else:
        return False

def keyPress(e):

    br = c.bbox(rec)
    bo = c.bbox(obstacle)
    global xx
    global yy

    if e.keysym == "Up":
        xx = 0
        yy = -5
        if detectCollision() == False:
            coords = c.coords(rec)
            x=0
            y=-5
            c.move(rec,x,y)

    elif e.keysym == "Right":
        xx = 5
        yy = 0
        if detectCollision() == False:
            coords = c.coords(rec)
            x=5
            y=0
            c.move(rec,x,y)    

    elif e.keysym == "Down":
        xx = 0
        yy = 5
        if detectCollision() == False:
            coords = c.coords(rec)
            x=0
            y=5
            c.move(rec,x,y)

    elif e.keysym == "Left":
        xx = -5
        yy = 0
        if detectCollision() == False:
            coords = c.coords(rec)
            x=-5
            y=0
            c.move(rec,x,y) 

                        
        

        

    
w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)



w.mainloop()
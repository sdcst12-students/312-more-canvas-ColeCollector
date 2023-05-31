import tkinter as tk

"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map1.txt','r')
x=0
Walls = []

while True:
    Walls.append(f.readline())
    x = x+1
    if x>15:
        print(Walls)
        break

print(len(Walls))



w.mainloop()
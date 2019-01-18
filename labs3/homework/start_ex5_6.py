from turtle import *

def draw_star(x,y,length):
    penup()
    setpos(x,y)
    pendown()

    for j in range(5):
        forward(length)
        right(144)
    return x,y,length

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()
from turtle import *
shape("arrow")

def draw_square(lengh,col):
    color(col)
    for j in range(4):
        forward(lengh)
        left(90)
    return(lengh,col)


for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()




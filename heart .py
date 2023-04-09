import turtle
turtle.bgcolor("black")
turtle.speed(1000)
turtle.pensize(10)
def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
turtle.color('red' ,'black')
turtle.begin_fill()
turtle.right(221.1)
turtle.forward(140)

func()
turtle.left(130)
func()
turtle.forward(140)
turtle.end_fill()
turtle.hideturtle()
for i in range(10):
    turtle.circle(10)
turtle.done()




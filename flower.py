import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.title("flower")
s.bgcolor('black')
t.speed(0)
col=['white','gold','red','cyan','blue','silver','pink']
for i in range(120):
    t.pencolor(col[i%6])
    t.circle(190-i/2,90)
    t.lt(90)
    t.circle(190-i/3,90)
    t.lt(60)
s.exitonclick()
turtle.done()

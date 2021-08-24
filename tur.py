import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('Black')
t.width(4)
t.speed(30)

col = ('yellow','red','white','blue')

for i in range (300):
    t.pencolor(col[i%4])
    t.forward(i*4)
    t.right(137)
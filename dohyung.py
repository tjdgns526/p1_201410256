
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
width=t1.window_width()
height=t1.window_height()
width
height
def drawTriangleAt():
 t1.penup()
 t1.goto(-320,150)
 t1.pendown()
 t1.goto(-400,-150)
 t1.goto(-240,-150)
 t1.goto(-320,150)
def drawPolygon():
 t1.penup()
 t1.goto(0,150)
 t1.pendown()
 t1.goto(-100,50)
 t1.goto(-50,-150)
 t1.goto(50,-150)
 t1.goto(100,50)
 t1.goto(0,150)
def drawStar():
 t1.penup()
 t1.goto(320,150)
 t1.pendown()
 t1.goto(270,-150)
 t1.goto(420,0)
 t1.goto(220,0)
 t1.goto(370,-150)
 t1.goto(320,150)
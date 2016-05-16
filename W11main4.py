import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()
t1.circle(100)
cen=(0,100)
radius=100
curpos=(0,0)

def isInCircle(curpos,radius,cen):
    if math.sqrt(pow(cen[0]-curpos[0],2)+pow(cen[1]-curpos[1],2))<radius:
        t1.pencolor("Red")
        print "Turtle's In"
    else:
        t1.pencolor("Black")
        print "Turtle's Out"

def keyup():
    t1.fd(30)
    tp=t1.pos()
    isInCircle(tp,radius,cen)
    
def keydown():
    t1.back(30)
    tp=t1.pos()
    isInCircle(tp,radius,cen)

def keyleft():
    t1.left(30)
def keyright():
    t1.right(30)
def mousegoto(x,y):
    t1.setpos(x,y)
    tp=t1.pos()
    isInCircle(tp,radius,cen)



def addmouse():
    wn.onclick(mousegoto)

def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")

def playgame():
    addkeys()
    addmouse()
    wn.listen()
    turtle.mainloop()
playgame()
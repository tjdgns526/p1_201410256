import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
coord=[(50,100),(100,100)]
curpos=(0,0)

def isonLine(curpos,coord):
    if coord[0][0]-1<=curpos[0]<=coord[1][0]+1 and coord[0][1]-1<=curpos[1]<=coord[1][1]+1:
        t1.pencolor("Red")
        print "Turtle's On"
    else:
        t1.pencolor("Black")
        print "Turtle's Out"

def keyup():
    t1.fd(30)
    tp=t1.pos()
    isonLine(tp,coord)
    
def keydown():
    t1.back(30)
    tp=t1.pos()
    isonLine(tp,coord)
    
def keyleft():
    t1.left(30)
def keyright():
    t1.right(30)
def mousegoto(x,y):
    t1.setpos(x,y)
    tp=t1.pos()
    isonLine(tp,coord)


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


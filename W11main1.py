import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("myMaze.gif")
def keyup():
    t1.fd(30)
    
def keydown():
    t1.back(30)
def keyleft():
    t1.left(30)
def keyright():
    t1.right(30)

def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")

def playgame():
    addkeys()
    wn.listen()
    turtle.mainloop()
playgame()



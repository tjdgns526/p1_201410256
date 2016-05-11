import turtle
wn = turtle.Screen()
t1= turtle.Turtle()

def squareMaking():
    t1.fd(50)
    t1.left(90)
    t1.fd(50)
    t1.left(90)
    t1.fd(50)
    t1.left(90)
    t1.fd(50)

def keyup():
    t1.fd(50)

def keydown():
    t1.back(50)

def keyleft():
    t1.left(90)

def keyright():
    t1.right(90)

def mousegoto(x,y):
    t1.setpos(x,y)

def mousepos(x,y):
    if 0<x and x<50:
        if 0<y and y<50:
            print "Here"
 
def keyquit():
    wn.bye()

def addKeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")
    wn.onkey(keyquit,"q")

def addMouse():
    wn.onclick(mousegoto)
    wn.onclick(mousepos)
def lab11():
    squareMaking()
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()

def main():
    lab11()

if __name__=="__main__":
    main()
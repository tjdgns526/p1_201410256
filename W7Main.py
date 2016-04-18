import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def drawSquareAtSave(size,pos):
    tracks=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.left(90)
        tracks.append(t1.pos())
    print tracks
drawSquareAtSave(100,(0,0))
def lab7():
    drawSquareAtSave(size,pos)
    
def main():
         lab7()

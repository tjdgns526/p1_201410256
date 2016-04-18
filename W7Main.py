import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
tracks=list()
def drawSquareAtSave(size,pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.left(90)
        tracks.append(t1.pos())
    return tracks
def drawSquareFromList(tracks):
    for i in range(4):
        t1.goto(tracks[i])
def lab7():
    drawSquareAtSave(100,(0,0))
    t1.clear()
    print tracks
    drawSquareFromList(tracks)
def main():
    lab7()

if __name__=="__main__":
    main()

def drawSquareAtSave(size,pos):
    ﻿import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    tracks=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.left(90)
        tracks.append(t1.pos())
    return tracks
def drawSquareFromList(tracks):
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    for i in range(4):
        t1.goto(tracks[i])
def saveTracks():
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.speed(1)
    t1.penup()
    tracks = list()
    t1.goto(-400,300)
    tracks.append(t1.pos())
    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(400)
    tracks.append(t1.pos())
    t1.backward(150)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(150)
    tracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    tracks.append(t1.pos())
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(100)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(200)
    tracks.append(t1.pos())
    return tracks
def replayTracks(myTrack):
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    for i in range(0,len(myTrack)):
        t1.goto(myTrack[i])

def lab7():
    myList=drawSquareAtSave(100,(0,0))
    drawSquareFromList(myList)
    myTrack = saveTracks()
    replayTracks(myTrack)
def main():
    lab7()

if __name__=="__main__":
    main()

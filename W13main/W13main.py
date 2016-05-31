%%writefile test.txt
0,0,10,10
20,20,30,30

def getCoordsFromFile(filename):
    fin1=open(filename,'r')
    mycoords=[]
    test1=list()
    for line in fin1:
        word= line.split(',')
        aRect=[(float(word[0]),float(word[1])),(float(word[2]),float(word[3].strip()))]
        mycoords.append(aRect)
    fin1.close()
    print mycoords
    return mycoords

import turtle
wn=turtle.Screen()
t2=turtle.Turtle()
def drawSquareWithCoords(coords):
    t2.home()
    t2.clear()
    t2.penup()
    
    for i in range(len(coords)):
        t2.goto(coords[i][0][0],coords[i][0][1])
        t2.pendown()
        t2.fd(coords[i][1][0]-coords[i][0][0])
        t2.left(90)
        t2.fd(coords[i][1][1]-coords[i][0][1])
        t2.left(90)
        t2.fd(coords[i][1][0]-coords[i][0][0])
        t2.left(90)
        t2.fd(coords[i][1][1]-coords[i][0][1])
        t2.penup()
        t2.home()


def lab13():
	getCoordsFromFile('test.txt')
	drawSquareWithCoords(getCoordsFromFile('test.txt'))


def main():
	lab13()


if__name__=="__main__":
	main()
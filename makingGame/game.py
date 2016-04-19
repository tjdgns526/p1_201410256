import turtle
import random
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.pencolor("red")
oldhead=t1.heading()
t1point=0
t2point=0
wn.bgpic("picture2.gif")

x=tuple
x=((670,-400),(670,-200),(670,0),(670,200),(670,400),(370,400),(70,400),(-230,400),(-430,400,),(-730,400),(-730,200),(-730,0),(-730,-200),(-730,-400),(-430,-400),(-230,-400,),(70,-400),(370,-400),(670,-400),(670,-400),(670,-400))

i=0
j=0
t1.penup()
t2.penup()
t1.setpos(x[i])
t2.setpos(x[j])

def drawStarforplayer1():
    t1.setpos(0,0)
    t1.setheading(oldhead)
    t1.pendown()
    t1.fd(100)
    t1.right(144)
    t1.fd(100)
    t1.right(144)
    t1.fd(100)
    t1.right(144)
    t1.fd(100)
    t1.right(144)
    t1.fd(100)

def drawStarforplayer2():
    t2.setpos(0,0)
    t2.setheading(oldhead)
    t2.pendown()
    t2.fd(100)
    t2.right(144)
    t2.fd(100)
    t2.right(144)
    t2.fd(100)
    t2.right(144)
    t2.fd(100)
    t2.right(144)
    t2.fd(100)

while i<=18 and j<=18:
    print "Player 1, Test your Luck. If you ready, press Enter"
    ask1=raw_input ("Are you ready?")
    a=random.randrange(1,3)
    print "Player 1 Number:", a
    print " "
    print "Player 2, Test your Luck. Press Enter"
    ask1=raw_input ("Are you ready?")
    b=random.randrange(1,3)
    print "Player 2 Number:", b
    print " "
    if a>b:
  	print "Player 1 gets points"
        if a==3:
            i=i+3
            t1.setpos(x[i])
            if i%3==0:
                t1point = t1point +300
            elif i%2==0:
                t1point = t1point +200
            else:
                t1point = t1point +100
        else:
            i=i+2
            t1.setpos(x[i])
            if i%3==0:
                t1point = t1point +300
            elif i%2==0:
                t1point = t1point +200   
            else: t1point = t1point +100    
    elif a==b:
        print "Same number, Don't move and Two players get 100 points each. "
        t1point = t1point + 100;
        t2point = t2point + 100;

    else:
        print "Player 2 gets points"
        if b==3:
            j=j+3
            t2.setpos(x[j])
            if j%3==0:
                t2point = t2point +300
            elif j%2==0:
                t2point = t2point +200
            else:
                t2point = t2point +100
        else:
            j=j+2
            t2.setpos(x[j])
            if j%3==0:
                t2point = t2point +300
            elif j%2==0:
                t2point = t2point +200   
            else: t2point = t2point +100
    print " "
    print "Player 1 points = ", t1point 
    print "Player 2 points = ", t2point
    print " "

print " "
print " Final Player 1 points are ", t1point
print " Final Player 2 points are ", t2point

if t1point>t2point:
    print "Player 1 win !"
    drawStarforplayer1()
    t2.shape("turtle")
elif t1point==t2point:
    print "Draw!"
else:
    print "Player 2 win !"
    drawStarforplayer2()
    t1.shape("turtle")
wn.exitonclick()
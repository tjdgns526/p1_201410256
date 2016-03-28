import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.home()
t1.clear()
def Baram(size,bigger,turns,angle):
    
    for i in range(0,turns):
        if(i%2):
            size+=bigger
        t1.forward(size)
        t1.right(angle)

Baram(100,100,10,90)
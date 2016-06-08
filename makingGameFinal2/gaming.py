import turtle
import random
def playgame():
    print "======================================================="
    print "Test Your Luck"
    print "You must be on one district!!!"
    print "The number on the area means how strong your luck is"
    print "======================================================="
    pn=raw_input("Input your name:") 
    wn=turtle.Screen()
    wn.bgpic("background2.gif")
    naming=[]
    scoring=[]
    t1=turtle.Turtle()
    t1.shape("turtle")
    wn.setup(500,500)
    global score
    curpos=(0,0)
    tp=t1.pos()
    score = 100
    opp=11
    coord=[(-250,250),(0,0),(250,250),(-250,-250),(250,-250)]
    def gam1():
        global score
        print "You Chose Number 1"
        if random.random()<=0.9:
            score = score + 20
            print "My Score is",score
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score
        else:
            score = score - 5
            print "My Score is",score
            print score
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score
    def gam2():
        global score
        print "You Chose Number 2"
        if random.random()<=0.5:
            score = score + 50
            print "My Score is",score
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score
        else:           
            score = score - 10
            print "My Score is",score
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score
    def gam4():
        global score
        print "You Chose Number 4"
        if random.random()<=0.25:
            score = score + 80
            print "My Score is",score
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score   
        else:            
            score = score - 20
            print "My Score is",score  
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score    
    def gam8():
        global score
        print "You Chose Number 8"
        if random.random()<=0.125:
            score = score +100
            print "My Score is",score           
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score 
        else:
            score = score - 30 
            print "My Score is",score           
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score
    def gamble(curpos,coord):     
        global score
        an=raw_input("If you Ready, press any buttons")
        if (coord[0][0]<curpos[0]<coord[1][0] and coord[1][1]<curpos[1]<coord[0][1]):
            gam4()
        elif (coord[1][0]<curpos[0]<coord[2][0] and coord[1][1]<curpos[1]<coord[2][1]):
            gam1()
        elif (coord[3][0]<curpos[0]<coord[1][0] and coord[3][1]<curpos[1]<coord[1][1]):
            gam2()
        elif (coord[1][0]<curpos[0]<coord[4][0] and coord[4][1]<curpos[1]<coord[1][1]):
            gam8()
        else:
            print "START"
    def groundSetting():
        t1.pencolor("YELLOW")
        t1.width(5)
        t1.fd(250)
        t1.back(500)
        t1.fd(250)
        t1.left(90)
    	t1.fd(250)
    	t1.back(500)
    	t1.fd(250)
    	t1.penup()
    def writeRank(user,score):
        fin=open('ranking.txt','w')
        naming.append(user)
        scoring.append(score)
        for i in range(0,len(naming)):
            fin.write("NAME: {0} POINT: {1} \n".format(naming[i],scoring[i]))
        fin.close()
    def readRank():
        fout=open('ranking.txt','r')
        for line in fout:
            print line
    	fout.close()
    def keyup():
        t1.forward(45)
    def keyleft():
        t1.left(45)
    def keyright():
        t1.right(45)
    def keydown():
        t1.back(45)
    def addKeys():
        wn.onkey(keyup, "Up")
        wn.onkey(keyleft, "Left")
        wn.onkey(keyright, "Right")
        wn.onkey(keydown, "Down")
    def mousegoto(x,y):
        t1.setpos(x,y)
    def addmouse():
        wn.onclick(mousegoto)   
    groundSetting()
    addmouse()
    addKeys()
    gamble(tp,coord)
    while(opp>0):
        gamble(tp,coord)
        tp=t1.pos() 
        opp = opp -1
        print opp,"times left."
        if (100<score<200):
            t1.color("ORANGE")
        elif(200<=score<300):
            t1.color("YELLOW")
        elif(score>=300):
            t1.color("RED")
        else:
            t1.color("GREY")
    writeRank(pn,score)
    readRank()
    wn.listen()
    turtle.mainloop()
playgame()

def main():
    playgame()
main()
import turtle
import random
def playgame():
    print "Test Your Luck"
    print "You can Click the area"
    print "The number on the area means how strong your luck is"
    pn=raw_input("Input your name") 
    wn=turtle.Screen()
    wn.bgpic("background.gif")
    naming=[]
    scoring=[]
    t1=turtle.Turtle()
    t1.shape("turtle")
    wn.setup(500,500)
    point = 100
    opp=10
    coord=[(-250,250),(0,0),(250,250),(-250,-250),(250,-250)]
    def gam1(score):
        if random.random()<=0.9:
            score = score + 10
            print "My Score is"
            print score
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score
        else:
            score = score - 10
            print "My Score is"
            print point
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score
    def gam2(score):
        if random.random()<=0.5:
            score = score * 2
            print "My Score is"
            print score
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score
        else:
            score = score - 30
            print "My Score is"
            print score   
            t1.shapesize(score*0.01,score*0.01,score*0.01)
           return score
    def gam4(score):
        if random.random()<=0.25:
            score = score * 4
            print "My Score is"   
    def gam8(score):
        if random.random()<=0.125:
            score = score * 8
            print "My Score is" 
            print score            
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score 
        else:
            score = score - 80 
            print "My Score is"
            print score           
            t1.shapesize(score*0.01,score*0.01,score*0.01)
            return score
    def groundSetting():
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
            fin.write("NAME: {0} POINT: {1}\n".format( scoring[i], naming[i]))
        fin.close()
    def readRank():
        fout=open('ranking.txt','r')
        for line in fout:
            print line
    	fout.close()
    def gamble(curpos,coord,score):
        an=raw_input("If you Ready, press any button")
        if coord[0][0]<curpos[0]<coord[1][0] and coord[1][1]<curpos[1]<coord[0][1]:
            gam4(score)
            point=gam4(score)
        elif coord[1][0]<curpos[0]<coord[2][0] and coord[1][1]<curpos[1]<coord[2][1]:
            gam1(score)
            point=gam1(score)
        elif coord[3][0]<curpos[0]<coord[1][0] and coord[3][1]<curpos[1]<coord[1][1]:
            gam2(score)
            point=gam2(score)
        elif coord[1][0]<curpos[0]<coord[4][0] and coord[4][1]<curpos[1]<coord[1][1]:
            gam8(score)
            point=gam8(score)
        print score
    def mousegoto(x,y):
        t1.setpos(x,y)
        tp=t1.pos()
    def addmouse():
        wn.onclick(mousegoto)   
    groundSetting()
    addmouse()
    tp=t1.pos()
    while(opp>0 and point>=0):
        print opp 
        print "times left."
        gamble(tp,coord,score)
        opp = opp -1
    wn.listen()
    turtle.mainloop()
def main():
    playgame()
main()
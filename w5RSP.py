User=raw_input("User Choose?(Scissor=1,Rock=2,Paper=3):")
Com=raw_input("Computer Choose?(Scissor=1,Rock=2,Paper=3:)")

def RSP():
    if User=='1':
        if Com=='1':
            print "Draw."
        if Com=='2':
            print "Computer Win"
        if Com=='3':
            print "User win."
    elif User=='2':
        if Com=='1':
            print "User win."
        if Com=='2':
            print "Draw."
        if Com=='3':
            print "Computer Win."
    elif User=='3':
        if Com=='1':
            print "Computer Win."
        if Com=='2':
            print "User win."
        if Com=='3':
            print "Draw."
RSP()

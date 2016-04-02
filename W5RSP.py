User=raw_input("User Choose?(Scissor=1,Rock=2,Paper=3):")
Com=raw_input("Computer Choose?(Scissor=1,Rock=2,Paper=3:)")

def RSP():
    if User=='1':
        if Com=='1':
            print "서로 비겼습니다."
        if Com=='2':
            print "컴퓨터가 이겼습니다."
        if Com=='3':
            print "내가 이겼습니다."
    elif User=='2':
        if Com=='1':
            print "내가 이겼습니다."
        if Com=='2':
            print "서로 비겼습니다."
        if Com=='3':
            print "컴퓨터가 이겼습니다."
    elif User=='3':
        if Com=='1':
            print "컴퓨터가 이겼습니다."
        if Com=='2':
            print "내가 이겼습니다."
        if Com=='3':
            print "서로 비겼습니다."
RSP()
"""
@author:KSH
Date:2016.04.06
"""

def sumOfMultiplesOf3_5():
    print "As1_sumOfMultiplesOf3_5"
    sum=0
    begin=raw_input("Please Input the First value:")
    End=raw_input("Please Input the Last value:")
    begin=int(begin)
    End=int(End)
    for i in range(begin,End):
             if (i%3==0 or i%5==0):
                 sum=sum+i
             elif(i%15==0):
                 sum=sum-i
    print "The answer is",
    print sum



def FindingLeapYear():
    print "As2_Finding LeapYear"
    year=raw_input("Input the year:")
    year=int(year)
    
    if(year%4 == 0) and (year % 100 !=0 or year % 400==0):
        res="LeapYear"
    else:
        res="Not LeapYear"
    print "The answer is",
    print res

def UpAndDown():
    print "As3_It's the UpAndDownGame!"
    num1=raw_input("The answer is:")
    num1=int(num1)

    for i in range(100):
        num2=raw_input("Guess the number:")
        num2=int(num2)
        if num2>num1:
            print "Down"
        elif num2<num1:
            print "UP"
        elif num2==num1: 
            print "Correct"
            break

"""
20160411 Additional Assignment
"""

x1=list()
for i in range(0,1000):
    if(i%4==0) and (i%5!=0):
       x1.append(i)
def sumList(list):
    sum=0
    for i in range(0,len(list)):
        sum+=list[i]
    print "The sum of list is",
    print sum

def lab3():
    sumOfMultiplesOf3_5()
    FindingLeapYear()
    UpAndDown()
    sumList(x1)
def main():
	lab3()

if __name__=="__main__":
	main()
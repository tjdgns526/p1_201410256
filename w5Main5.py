def ComputeGrade(Marks):
    if (90<=Marks<=100):
        grade= 'A'
    elif(80<=Marks<90):
        grade= 'B'
    elif (70<=Marks<80):
        grade= 'C'
    elif (60<=Marks<70):
        grade= 'D'
    elif (Marks<60):
        grade= 'F'
    return grade

MarksTmp = raw_input("Enter Your Marks(0~100):")
Marks=float(MarksTmp)
mygrade=ComputeGrade(Marks)
print mygrade

exitonclick()


     
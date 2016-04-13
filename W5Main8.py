def ComputeBMI(height,weight):
     BMI=weight/(height*height)
     if(BMI<18.5):
         res="LowWeight"
     elif(18.5<=BMI<23):
         res="Normal"
     elif(23<=BMI<25):
         res="OverWeight"
     elif(25<=BMI<30):
         res="Obesity"
     elif(30<=BMI):
         res="OverObesity"
     else:
         res="Error! Please just value"
     print res

ComputeBMI(1.8,80)

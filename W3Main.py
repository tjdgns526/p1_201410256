def Converttem():
    cf=raw_input("Choose! celsius or fahrenheit: ")

      if(cf=='c'):
           print "You entered celsius, enter It's value"
           temp=raw_input("celsius value: ")
           fahtemp=float(temp)
           tem=(fahtemp *1.8)+32
           print tem
      else:
       print "You entered fahrenheit, enter it's value"
       temp = raw_input("fahrenheit value: ")
       celtemp=float(temp)
       tem=(celtem-32)/1.8
       print tem
       

Converttem()

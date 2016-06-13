class Dog(object):
    def __init__(self,name):
        name="dog"
        sound='mong mong'
    def bark(self):
        print self.sound


class Sichu(Dog):
    name='Sichu'
    sound='si Chu!'

class PitBul(Dog):
    name='PitBul'
    sound='pit~Bul!'

dog2=Sichu("Mac")
dog3=PitBul("Bill")
dog2.bark()
dog3.bark()

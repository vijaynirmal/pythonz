class Dog(object):
    def __init__(self):
        self.hungry = 1
    def eat(self):
        if self.hungry :
            print ("Gimme food buster!")
            self.hungry = 0
        else :
            print("Im full :)")

class FunnyBird(Dog):
    def __init__(self):
        super(FunnyBird,self).__init__()
        self.song = 'scoobydooby dooo'
        print(self.song)

fb = FunnyBird()
fb.eat()
fb.eat()

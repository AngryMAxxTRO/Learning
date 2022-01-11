import turtle

class items:
    pass

class live(items):
    pass

class nonlive(items):
    pass

class road(nonlive):
    pass

class animal(live):
    def breeze(self):
        print("Breathing")
    def move(self):
        print("Moving")
    def eat(self):
        print("Eating")

class big(animal):
    def child(self):
        print("Running")

class giraffe(big):
    def feeding(self):
        print("Nom-nom")
    def findfood(self):
        self.move()
        print("Searching food")
        self.feeding()
        print("Found some food")
    def eat_plant(self):
        self.feeding()
    def dance(self):
        self.move()
        self.move()
        self.move()
        self.move()
        
donald = giraffe()
harold = giraffe()

donald.eat()
harold.move()
donald.findfood()

'''
avery = turtle.pen()
kate = turtle.pen()

avery.forward(50)
avery.right(90)
avery.forward(20)

kate.left(90)
kate.forward(100)

jacob = turtle.pen()
jacob.left(180)
jacob.forward(80)
'''

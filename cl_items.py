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
    def left_leg_forward(self):
        print('Left leg rorward')
    def left_leg_backward(self):
        print('Left leg backward')
    def right_leg_forward(self):
        print('Right leg forward')
    def right_leg_backward(self):
        print('Right leg backward')
    def dance_move(self):
        self.left_leg_backward()
        self.left_leg_forward()
        self.right_leg_forward()
        self.right_leg_backward()
        self.left_leg_backward()
        self.right_leg_backward()
        self.right_leg_forward()
        self.left_leg_forward()

donald = giraffe()
harold = giraffe()
mike = giraffe()

donald.eat()
harold.move()
donald.findfood()
mike.dance_move()

class giraffe:
    def __init__(self, marks):
        self.giraffe_marks = marks

osvald = giraffe(100)
gertrude = giraffe(200)

print(osvald.giraffe_marks)
print(gertrude.giraffe_marks)

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

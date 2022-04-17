import turtle


class Items:
    pass


class Live(Items):
    pass


class NonLive(Items):
    pass


class Road(NonLive):
    pass


class Animal(Live):
    def breeze(self):
        print("Breathing")

    def move(self):
        print("Moving")

    def eat(self):
        print("Eating")


class Big(Animal):
    def child(self):
        print("Running")


class Giraffe(Big):
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
        print('Left leg forward')

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


donald = Giraffe()
harold = Giraffe()
mike = Giraffe()

donald.eat()
harold.move()
donald.findfood()
mike.dance_move()


class Giraffe:
    def __init__(self, marks):
        self.giraffe_marks = marks


osvald = Giraffe(100)
gertrude = Giraffe(200)

print(osvald.giraffe_marks)
print(gertrude.giraffe_marks)

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

import sys
def weight():
    print("Enter mass")
    mass = int(sys())
    massp = int(sys())
    for i in range(15):
        mass = mass + massp
        print(round(mass * 0.165, 1))
        print(mass, massp)
weight()
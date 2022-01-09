import sys
def weight():
    print("Enter mass")
    mass = int(sys.stdin.readline())
    massp = float(sys.stdin.readline())
    for i in range(15):
        mass = mass + massp
        print(round(mass * 0.165, 2))
weight()
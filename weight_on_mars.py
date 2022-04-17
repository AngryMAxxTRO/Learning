import sys


def weight():
    print("Enter mass")
    mass = int(sys.stdin.readline())
    print("Enter massp")
    massp = float(sys.stdin.readline())
    print("Enter years")
    years = int(sys.stdin.readline())
    for i in range(years):
        mass = mass + massp
        print("Your mass on the moon is %s in year %s" % (round(mass * 0.165, 2), i + 1))


weight()

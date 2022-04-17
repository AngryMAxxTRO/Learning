import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if (a + b) <= c:
    print("not triangle")
elif (a + c) <= b:
    print("not triangle")
elif (b + c) <= a:
    print("not triangle")
else:
    print("triangle")

import sys

arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])

if arg1 < 0 or arg1 > 999999 and arg2 < arg1 or arg2 > 999999:
    print("Out of range")
    exit()

x = []

for lst in range((arg2 + 1) - arg1):
    y = str(lst + arg1)
    x.append("0" * (6 - len(y)) + y)

print(x)

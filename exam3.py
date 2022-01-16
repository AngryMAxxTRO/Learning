import sys

args = sys.argv[1]

x = 0

for letter in args:
    if x < 0:
        break
    elif letter == "(":
        x += 1
    elif letter == ")":
        x -= 1
if x != 0:
    print("NO")
else:
    print("YES")

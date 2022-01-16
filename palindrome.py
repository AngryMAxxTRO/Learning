import sys

string = str(sys.argv[1]).lower().replace(" ", "")

if string == string[::-1]:
    print("YES")
else:
    print("NO")

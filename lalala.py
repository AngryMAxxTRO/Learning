import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

print("Everybody sing a song:" + ((" " + (a - 1) * "la-" + "la") * b) + ((c * 1) * "!") + (1 - c) * ".")
import sys

args = len(sys.argv)

x = []

for list in range (1, args):
    x.append(sys.argv[list])

x.reverse()

print(' '.join(x))

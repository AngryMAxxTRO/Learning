import sys

args = len(sys.argv)

x = []

for lst in range(1, args):
    x.append(sys.argv[lst])

x.reverse()

print(' '.join(x))

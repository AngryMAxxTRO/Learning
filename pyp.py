import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

x = (1 / (c * math.sqrt(2 * math.pi)) * math.exp(- ((a - b) ** 2) / (2 * c ** 2)))

print(round(x, 11))

import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

print(math.sqrt(a * b) / (math.exp(a) * b) + a * math.exp(2 * a / b))

import sys

counter = int(sys.argv[1])
a = 1
result = 0

for fib in range(counter):
    a, result = result, a + result

print(result)

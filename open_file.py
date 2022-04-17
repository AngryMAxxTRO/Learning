file = open("file.txt", "r")
print(file.readable())
print(file.read())
file.close()

file = open("file.txt", "a")
file.write("\nSeven")
file.close()


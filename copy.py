from venv import create


test_file = open("file.txt")
copy_file = open("copy.txt", "w")
copy_file.write(test_file.read())
copy_file.close()
read_file = open("copy.txt")
print(read_file.read())
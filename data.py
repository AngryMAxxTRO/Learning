import pickle

data = {
    "numbers" : 878.65,
    "items" : ["item1", "item2", "item3"],
    "position" : "pos45"
}

file = open("save.dat", "wb")
pickle.dump(data, file)
file.close()

saved_file = open("save.dat", "rb")
saved_data = pickle.load(saved_file)
saved_file.close()
print(saved_data)

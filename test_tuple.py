coordinates = (4, 5)
print(coordinates[1])


def say_hi(name, age):
    print("Hello User " + name + ' you are age ' + str(age))


say_hi("Mike", 19)


def cube(num):
    return num * num * num


result = cube(4)
print(result)

is_male = False
is_tall = True
if is_male and is_tall:
    print('You are a male and you tall')
elif is_male and not is_tall:
    print('You are a male and not tall')
elif not is_male and is_tall:
    print('You not a male and you tall')
else:
    print('You are not a male')

friends = ["Jim", "Karen", "Kevin"]
len(friends)
for letter in "Giraffe":
    print(letter)
for name in friends:
    print(name)
for index in range(3, 10):
    print(index)
for index in range(len(friends)):
    print(friends[index])
for index in range(5):
    if index == 0:
        print("First")
    else:
        print("Not first")

print(2 ** 3)


def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 4))

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])
for row in number_grid:
    print(row)
    for col in row:
        print(col)

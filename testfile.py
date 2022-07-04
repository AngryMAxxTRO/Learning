a = '8 j 8   mBliB8g  imjB8B8  jl  B'
b = "".join(a.split())
c = a.replace(' ', '')
print(b)
print(c)

nums = 35231
e = [int(i) for i in reversed(str(nums))]
print(e)


def positive_sum(arr):
    # Your code here
    x = 0
    for i in arr:
        if i <= 0:
            continue
        else:
            x += i
    return x


print(positive_sum([1, 2, 3, 4, 5]))


def maps(d):
    return [i * 2 for i in d]


print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


def disemvowel(string):
    text = ''
    for i in string:
        if i.lower() == 'a':
            continue
        elif i.lower() == 'e':
            continue
        elif i.lower() == 'i':
            continue
        elif i.lower() == 'o':
            continue
        elif i.lower() == 'u':
            continue
        else:
            text += i
    return text


print(disemvowel("This website is for losers LOL!"))


def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


print(disemvowel("This website is for losers LOL!"))

a = 2
b = 2
c = 5
print(bin(a + b).replace('0b', ''))
print(c - c - c)


def past(h, m, s):
    # Good Luck!
    return h * ((60 * 60) * 1000) + m * (60 * 1000) + s * 1000


print(past(0, 1, 1))

task = "ZpglnRxqenU"


def accum(s):
    count = 0
    out = []
    for i in s.lower():
        count += 1
        out.append((i * count).capitalize())
    return '-'.join(out)


print(accum(task))

year = 1901

if year % 100 == 0:
    print(year // 100)
else:
    print(year // 100 + 1)

test = [1, 2, 'a', 'b', 1, 'a', 'b', 0, 15]

for i in test * 1:
    if not type(i) == int:
        test.pop(test.index(i))

print(test)

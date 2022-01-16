from ntpath import join


a = abs(10) + abs(-10)
b = abs(-10) + -10
print(a, b)

sometext = "Це якщо не ти дуже це хороший читаєш спосіб то заховати щось повідомлення негаразд"
lst = sometext.split(' ')
somestring = ' '.join(lst[::2])
print(somestring)
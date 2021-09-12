def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase")))

# This program is cool
'''
Comment
Multiple 
Lines
'''
print("Comments are fun")

try:
    #value = 10 / 0
    number = int(input("Enter a number"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)

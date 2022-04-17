class Student:
    def __init__(self, name, major, gpa, is_on_prob):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_prob = is_on_prob

    def on_honor_roll(self):
        if self.gpa >= 3.1:
            return True
        else:
            return False


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes a onion rings")

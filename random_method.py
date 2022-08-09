import random

for i in range(3):
    print(random.random())  # print number randomly
    print(random.randint(10, 20))  # print int number randomly

languages = ['C', 'C++', 'C#', 'Python', 'JS', 'Java', 'PHP', 'Ruby', 'GO']
choosePL = random.choice(languages)
print(choosePL)


#  dice
class Dice:
    def __init__(self):
        self.first = random.randint(1, 6)
        self.second = random.randint(1, 6)

    def rolls(self):
        return self.first, self.second


dice = Dice()
print(dice.rolls())

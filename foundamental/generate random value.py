# import random

# random.random

# for i in range(6):
#     # print(random.random())
#     print(random.randint(20, 30))


# import random

# member = ['samuel', 'mcdavid', 'desmond', 'franklin']

# leader = (random.choice(member))
# print(leader)

import random 

class Dice:
   def roll (self):
       frist= random.randint(1,6)
       second = random.randint(1, 6)
       return frist, second

dice = Dice()
print(dice.roll())


import random


class Pick:
    
    def number(self):
        one = random.randint(1, 80)
        two = random.randint(1, 80)
        return one, two

even = Pick()
print(even.number())
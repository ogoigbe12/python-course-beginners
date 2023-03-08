class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('draw')
    def move(self):
        print('move')


point = Point(10,20)
point.x = 11
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'I am {self.name}')


samuel = Person('samuel ogoigbe')
samuel.talk()

no = Person('no wam')
no.talk()
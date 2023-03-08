class Animal:
    def walk(self):
        print('walk')

class Dog(Animal):
    def sit(self):
        print('sit')

class Cat(Animal):
    def get_out(self):
        print('get_out')


dog1 = Dog()
dog1.sit()

try:
    age = int(input('age: '))
    income = 5000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('age cannot be 0')
except ValueError:
    print('invaild value')

try:
    name = input('name: ')
    print(name)
except ValueError:
    print('incorrect input')
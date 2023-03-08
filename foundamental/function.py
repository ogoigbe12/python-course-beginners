def user_club():
    print('we made it to round 4')
    print('congratulation')


print('it been a long time coming')
user_club()
print('maining for the final')

# parameter in function

def user_vote(first_name, last_name):
    print(f'hello {first_name} {last_name} !')
    print('welcome aboard')


print('start')
user_vote('samuel', 'ogoigbe')
print('finish')

# keyword argument in function

def cat(junks, food, fruit):
    print(f'list an item each for {junks} {food} {fruit}')
    print('cat')


print('start')
cat('dotun', 'food= rice','fruit=orange')
print('is full')

# return statement in function

def square (number):
    return number * number

result = square(3)
print(result)

# 
def emoji_conv(message):
    words = message.split(" ")
    emojis = {
        ":)": "smile",
        ":(": "sad"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ""
        return output
    

message = input('>')
print(emoji_conv(message))



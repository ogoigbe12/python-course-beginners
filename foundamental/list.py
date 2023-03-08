def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


# 2D list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# matrix[0][1] = 20
# print(matrix[0][1])

# for row in matrix:
#     for item in row:
#         print(item)

# list method

number = [2, 5, 5, 6, 8, 9]
uni = []
for numbers in number:
    if number not in uni:
        uni.append(numbers)
print(uni)
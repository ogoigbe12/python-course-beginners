# for x in range(4):
#     for y in range(3):
#         print(f"{x}, {y}")


# number = [5, 2, 5, 2, 2]
# for x_count in number:
#     print('x'* x_count)

number = [1, 1, 1, 1, 5]
for x_count in number:
    output = ''
    for count in range (x_count):
        output += 'x'
    print(output)
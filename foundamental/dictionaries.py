# coustomer = {
#     'name': 'samuel ogoigbe',
#     'age': 21,
#     'is_confirm' : True
# }
# # print(coustomer['age'])
# print(coustomer.get('birth'))

phone = input('Phone: ')
dit_mapping = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four'
}

output = ""
for ch in phone:
    output += dit_mapping.get(ch, "!") + " "
print(output)

# def list(name):
#     name = ['samuel, ogoigbe']
#     print(samuel+ "" +ogoigbe)
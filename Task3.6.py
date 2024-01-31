def reverseLookup(dictionary, value):
    return [key for key, val in dictionary.items()
            if val == value]

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

value1 = 1
result1 = reverseLookup(my_dict, value1)
print(f'Keys for value {value1}: {result1}')

value2 = 3
result2 = reverseLookup(my_dict, value2)
print(f'Keys for value {value2}: {result2}')

value3 = 5
result3 = reverseLookup(my_dict, value3)
print(f'Keys for value {value3}: {result3}')

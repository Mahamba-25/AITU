negative_numbers = []
zeros = []
positive_numbers = []

while True:
    inp = input("Enter an integer: ")
    if inp == "":
        break
    number = int(inp)
    if number < 0:
        negative_numbers.append(number)
    elif number == 0:
        zeros.append(number)
    else:
        positive_numbers.append(number)
result = negative_numbers + zeros + positive_numbers

for value in result:
    print(value)

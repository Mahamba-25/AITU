sum = 0
inp = input("Please, enter the ages of the guests of the zoo\n")
while inp != "":
    val = int(inp)
    if val > 2 and val < 13:
       sum += 14
    elif val > 64:
        sum += 18
    elif val > 12 and val < 65:
        sum += 23
    inp = input()

print("Guests should pay $", format(sum, ".2f"))

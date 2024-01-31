a = int(input("Enter the number of sides of the figure\n"))
if a < 3 or a > 10:
    print("Please, enter number of sides between 3 and 10, including")
elif a == 3:
    print("Triangle")
elif a == 4:
    print("Square")
elif a == 5:
    print("Pentagon")
elif a == 6:
    print("Hexagon")
elif a == 7:
    print("Heptagon")
elif a == 8:
    print("Octagon")
elif a == 9:
    print("Enneagon")
elif a == 10:
    print("Decagon")

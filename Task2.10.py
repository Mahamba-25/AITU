inp = input("Enter the number to show multiplication table\n")
while inp != "":
    numb = int(inp)
    for i in range(1, 11):
        print(numb, "x", i, "=", numb * i)
    inp = input("Enter the number to show multiplication table\n")

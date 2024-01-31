s = input("Enter month name: ")
a = int(input("Enter day: "))
s = s.lower()
if s == "march":
    if a >= 20:
        print("Spring")
    else:
        print("Winter")
elif s == "june":
    if a < 21:
        print("Spring")
    else:
        print("Summer")    
elif s == "april" or s == "may":
    print("Spring")
    
elif s == "september":
    if a < 22:
        print("Summer")
    else:
        print("Autumn")
elif s == "july" or s == "august":
    print("Summer")
    
elif s == "december":
    if a < 21:
        print("Autumn")
    else:
        print("Winter")
elif s == "october" or s == "november":
    print("Autumn")
        
else:
    print("Winter last line")

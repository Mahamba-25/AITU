s = input("Enter the name of the month\n")
s = s.lower()
if s == "january" or s == "march" or s == "may" or s == "july" or s == "august" or s == "october" or s == "december":
    print("This month have 31 days")
elif s == "february":
    print("This month have 28 or 29 days")
else:
    print("This month habe 30 days")

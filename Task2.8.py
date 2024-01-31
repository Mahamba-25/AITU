val = int(input())
if val <= 2:
    sum = 0
elif val > 2 and val <= 12:
    sum = 14
elif val >= 65:
    sum = 18
else:
    sum = 23

print("$",round(sum, 2))

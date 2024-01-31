s = input()
a = 4.0
if "B" in s:
    a -= 1.0
elif "C" in s:
    a -= 2.0
elif "F" in s:
    a -= 4.0
elif "D" in s:
    a -= 3.0;
if "+" in s:
    a += 0.3
elif "-" in s:
    a -= 0.3
if s == "A" or s == "A+":
    print(4.0);
else:
    print(a)

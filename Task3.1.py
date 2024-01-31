n = int(input())
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
if n < 4:
    print("Error")
else:
    a.sort()
    a.remove(a[0])
    a.remove([0])
    a.remove(a[-1])
    a.remove(a[-1])
    

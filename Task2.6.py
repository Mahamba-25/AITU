a = int(input())
if a == 0:
    print("Error")
else:
    sum = a
    cnt = 1;
    while a != 0:
        sum += a
        cnt += 1
        a = int(input())
    print(sum/cnt)

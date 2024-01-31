inp = input("Enter a string: ")

cnt = {}
for i in inp:
    if i.isalnum():
        cnt[i.lower()] = 1

print("The number of unique characters is:", len(cnt))

import csv
columns = []
with open('AAPL.csv', mode = 'r', newline = '') as file:
    line = csv.reader(file)
    header = next(line)
    columns = [[] for _ in header]
    for row in line:
        for (i,v) in enumerate(row):
            columns[i].append(v)

s = input()
b = 0
for i in range(0,7):
    if s == header[i]:
        b = 1
        print(columns[i])
if b == 0:
    print("No such data")

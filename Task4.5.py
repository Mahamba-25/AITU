import csv
columns = []
with open('AAPL.csv', mode = 'r', newline = '') as file:
    line = csv.reader(file)
    header = next(line)
    columns = [[] for _ in header]
    for row in line:
        for (i,v) in enumerate(row):
            columns[i].append(v)
for i in columns[1]:
    print(i, "\n")

import csv

with open('AAPL.csv', mode = 'r', newline = '') as file:
    line = csv.reader(file)
    header = next(line)
    cnt = 1;
    for i in line:
        print(cnt, i)
        cnt += 1

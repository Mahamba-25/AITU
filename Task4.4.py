import csv
lines = []
with open('AAPL.csv', mode = 'r', newline = '') as file:
    something = csv.writer(file)
    lines = file.readlines()
print(lines)

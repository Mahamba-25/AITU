import csv

num_students = int(input("Enter the number of students: "))

student_data = []

for i in range(1, num_students + 1):
    numbeer = input(f"Enter Roll No for Student {i}: ")
    name = input(f"Enter Name for Student {i}: ")
    class_name = input(f"Enter Class for Student {i}: ")
    student_data.append([number, name, class_name])

with open('Student.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Rollno', 'Name', 'Class'])
    writer.writerows(student_data)

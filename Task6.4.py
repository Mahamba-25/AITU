class Employee:
    def __init__(self, name, ID, department, job):
        self.name = name
        self.ID = ID
        self.department = department
        self.job = job

    def get_info(self):
        print(self.name, self.ID, self.department, self.job)

if __name__ == "__main__":
    p = [
        Employee("Susan Meyers", 47899, "Acounting", "Vice President"),
        Employee("Mark Jones", 39119, "IT", "Programmer"),
        Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    ]

#    for i in range(0,3):
#        name = input("Enter name: ")
#        ID = input("Enter the ID: ")
#        department = input("Enter the departmennt where you work: ")
#        job = input("What is your job position: ")
#        p.append(name,ID,department,job)

    for i in range(0,3):
        p[i].get_info()
        
    

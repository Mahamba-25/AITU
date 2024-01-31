class Person:
    def __init__(self, name, address, age, number):
        self.name = name
        self.address = address
        self.age = age
        self.number = number
    def get_info(self):
        print(self.name, self.address, self.age, self.number)

if __name__ == "__main__":
    person1 = Person("Jim", "Mar Sara", 38, "822-275-SR1")
    person2 = Person("Arthas", "Northrend", 18, "no number")
    person3 = Person("Makhambet", "Almaty", 20, "+77757455347")
    person1.get_info()
    person2.get_info()
    person3.get_info()
    

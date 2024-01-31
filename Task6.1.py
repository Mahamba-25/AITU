class Pet:
    def __init__(self, name, animal, age):
        self.__name = name
        self.__animal = animal
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal(self, animal):
        self.__animal = animal

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__animal

    def get_age(self):
        return self.__age

if __name__ == "__main__":
    Stray = Pet("Stray", "cat", 3)
    print(Stray.get_name(), Stray.get_type(), Stray.get_age())
    name = input("Enter the name of your pet: ")
    animal = input("Enter the type of the animal: ")
    age = input("Enter the age of your pet: ")
    Another = Pet(name, animal, age)
    print(Another.get_name(), Another.get_type(), Another.get_age())

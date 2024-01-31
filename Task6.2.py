class Car:
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        print(self.__speed)

if __name__ == "__main__":
    car = Car(2011,"Toyota")
    for i in range(0,5):
        car.accelerate()
        car.get_speed()
    for i in range(0,5):
        car.brake()
        car.get_speed()

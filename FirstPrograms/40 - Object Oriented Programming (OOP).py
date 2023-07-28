
class Car:

    def __init__(self,make,model,year,color): # Equal to Constructor in other languages
        self.company = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"This {self.model} car is driving")

    def stop(self):
        print(f"This {self.model} car stopped driving")


car_one = Car("Chevy","Corvette",2021,"blue")
print(car_one.company)
print(car_one.model)
print(car_one.year)
print(car_one.color)

car_two = Car("Ford","Mustang",2022,"red")

car_two.drive()
car_two.stop()
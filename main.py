from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)


print(car2.model)
print(car2.year)
print(car2.color)
print(car2.forsale)

car1.drive()
car1.stop()
car1.describe()
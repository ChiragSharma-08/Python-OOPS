#Inheritance = Alows a class to inherit attributes and methods from another class
#              Helps with code reusability and extensibility
#              class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

class Dog(Animal):
    def speak(self):
        print("Woof!")
    pass

class Cat(Animal):
    def speak(self):
        print("Meow")
    pass

class Mouse(Animal):
    def speak(self):
        print("SQUEEK")
    pass

dog1 = Dog("Scooby")
dog2 = Dog("Bob")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog1.name)
print(dog2.name)
print(dog1.is_alive)
dog1.is_alive = False
print(dog1.is_alive)

dog2.speak()


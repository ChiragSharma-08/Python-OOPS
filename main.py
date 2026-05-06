#class variable = shared among all instances of a class
#                 Defined outside a constructor(construct = def __init__ in easy words)
#                 Allow you to share data among all objects created from that class

class Student:

    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Peter", 40)
student3 = Student("Pankaj", 50)


print(student1.name)
print(student1.age)
print(student1.class_year)
print(Student.class_year)

print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")

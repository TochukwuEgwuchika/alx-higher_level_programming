class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Student("Paul", 20)

print(a.__dict__)

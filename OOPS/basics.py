class Student:
    gender = "Female" #class variables (same)
    def __init__(self, name, age):
        self.name = name
        self.age = age #instance var(diff)

    def greet(self):
        print(f"Welcome {self.name}")

s = Student("Sreeja", 21)
s1 = Student("Cherry", 20)
s.greet()
s1.greet()
print(s.gender)
print(Student.gender)
print(s.name)
print(s.age)
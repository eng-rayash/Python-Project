class Person:
    def __init__(self, name):
        self.name = name
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name) # let the parent set the name
        self.salary = salary
emp = Employee("Sara", 5000)
print(emp.name, emp.salary)
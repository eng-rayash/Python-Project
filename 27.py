class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

dog1 = Dog("Rex", 3)
dog2 = Dog("Luna",5)

print(dog1.bark())
print(dog2.age)
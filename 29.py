class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return f"{self.name}: Meow"

class Dog(Animal):
    def speak(self):
        return f"{self.name}: Woof"

for animal in [Cat("Tom"), Dog("Rex")]:
    print(animal.speak())
class Animal:
    def __init__(self, name):
        self.name = name
        self.weight = 0

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.weight = 10

    def speak(self):
        print("woof")


class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.weight = 4

    def speak(self):
        print("meow")


class Bird(Animal):
    def __init__(self, name):
        super(Bird, self).__init__(name)
        self.weight = 0.5

    def speak(self):
        print("tweet")


class Fish(Animal):
    def __init__(self, name):
        super(Fish, self).__init__(name)
        self.weight = 0.2


animal = Animal("animal")
animal.speak()
print(animal.weight)

dog = Dog("dog")
dog.speak()
print(dog.weight)

cat = Cat("cat")
cat.speak()
print(cat.weight)

bird = Bird("bird")
bird.speak()
print(bird.weight)

fish = Fish("fish")
fish.speak()
print(fish.weight)
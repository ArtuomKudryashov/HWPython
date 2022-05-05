


class Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight= weight
        print(f"cat{self.name} is being initialized and says Meow!")


    def say_meow (self):
        print(F"{self.name}says Meow1")


black_cat = Cat(" Tom",2,8)



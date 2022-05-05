class Alive:
    breath = ""
    eat = ""
    reptoduce= ""

    def changeanimal(self, new_breath, new_eat, new_reproduce):
        self.breath = new_breath
        self.eat = new_eat
        self.reptoduce = new_reproduce




tiger= Alive()
tiger.eat
tiger.breath
tiger.reptoduce
print(tiger.changeanimal("lungs" , " meat" , "mammal"))
print(tiger.breath, tiger.eat,tiger.reptoduce)

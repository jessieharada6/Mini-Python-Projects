class Animal:
    def __init__(self):
        self.num_eyes = 2
        self.legs = 4

    def breathe(self):
        print("Inhale, exhale")

# inheritance
class Fish(Animal):
    def __init__(self):
        # inherit all attributes and methods from Animal class
        # The call to super() in the initialiser is recommended, but not strictly required.
        # as if the Animal object is already created but can be further modified
        super().__init__()
        self.skin = "blue"
        self.legs = 0

    def swim(self):
        print("moving in water")

    def breathe(self):
        # do everything from the parent breath class
        super().breathe()
        print("doing this under water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
print(nemo.skin)
print(nemo.legs)
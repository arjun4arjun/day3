class Animal:
    def __init__ (self,name):
        self.name= name

    def speak(self):
        print(f"{self.name} makes a sound")


class bird(Animal):
    def __init__(self, name):
        self.behaviour="playful"
        self.name= name

    def speak(self):
        print(f"{self.name} chirps and it is {self.behaviour}")

# animal= Animal("Catii")
# small_bird= bird("crow")
# small_bird.speak()
# animal.speak()

sprw=bird("sparrow")
sprw.speak()
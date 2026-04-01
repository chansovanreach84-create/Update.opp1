class pet:
    def __init__(self, name , hunger, energy, happiness):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
    
    def feed(self):      
        print(f"{self.name} is hungry !!")
    def play(self):
        print(f"{self.name} need to be {self.energy}!")
    def sleep(self):
        print(f"{self.name} really like {self.happiness}!")

pet1 = pet("Vath" , "burger" , "strong", "sleep")
pet1.feed()
pet1.play()
pet1.sleep()
        
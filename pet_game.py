class Pet:
    def __init__(self,name,fullness,happiness,sadness,fatness,boredom=0):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.sadness = sadness
        self.fatness = fatness
        self.boredom = boredom

    def feed_pet(self):
        self.fullness += 15
        self.fatness += 4
        self.happiness += 3
        self.sadness -= 2
        print(f"\n{self.name} has been fed a nice bowl of slop. Their fullness level is {self.fullness}.\n")

    def play_pet(self):
        self.happiness += 7
        self.sadness -= 3
        self.boredom -= 10
        print(f"\n{self.name} is so happy from the fun play time. Their happiness level is {self.happiness}.\n")

    def ignore_pet(self):
        self.sadness += 25
        self.boredom += 25
        print(f"\n{self.name} has been ignored. Their sadness level is {self.sadness}.\n")

    def stay_alive(self):
        self.fullness -= 4
        self.happiness -= 4
        self.sadness += 3
        self.fatness += 2
        self.boredom += 3

    def give_toy(self):
        self.happiness += 10
        self.sadness -= 5
        self.boredom -= 15
        print(f"\nYou have given {self.name} a toy! {self.name} is very happy!\n")

    def snuggle(self):
        self.happiness += 10
        self.sadness -= 5
        print(f"\nSnuggle time always improves {self.name}'s mood!\n")

    def exercise(self):
        self.happiness += 5
        self.fullness -= 5
        self.fatness -= 10
        self.sadness -= 2
        self.boredom -= 5
        print(f"\n{self.name} is shredding all that fat off with these intense exercises.\n")
    
    def treat(self):
        self.happiness += 10
        self.fullness += 5
        self.fatness += 15
        self.sadness -= 3
        self.boredom -= 3
        print(f"\nYummmm! {self.name} loves treats! {self.name} wants another treat!\n")

    def get_status(self):
        print(f"""
        Name: {self.name}
        Fullness: {self.fullness}
        Happiness: {self.happiness}
        Sadness: {self.sadness}
        Fatness: {self.fatness}
        Boredom: {self.boredom}
        """)



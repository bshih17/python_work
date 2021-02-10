class Fish:
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")

class Trout(Fish):
    def __init__(self, water = "freshwater"):
        self.water = water
        super().__init__(self)

fish = Trout('saltwater')
fish.swim()
fish.swim_backwards()
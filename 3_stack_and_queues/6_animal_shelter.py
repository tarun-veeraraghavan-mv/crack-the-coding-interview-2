"""
Animal SheltenAn animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat.You may use the built-in LinkedLis t data structure.
"""

from collections import deque

class AnimalShelter():
    def __init__(self):
        # remember in the queue structure we insert in the end using append() 
        # and remove from the end using a pop()
        self.dogs = []
        self.cats = []
        self.current_timestamp = 0

    def enqueue(self, name: str, animal_type: str):
        if animal_type == "dog":
            dog = {"name": name, "animal_type": animal_type, "timestamp": self.current_timestamp}
            self.dogs.append(dog)
        else:
            cat = {"name": name, "animal_type": animal_type, "timestamp": self.current_timestamp}
            self.cats.append(cat)

        self.current_timestamp += 1

    def dequeueAny(self):
        if not self.dogs or not self.cats:
            return None
        
        if not self.dogs:
            # pop(0) to remove the animal from the first index
            return self.cats.pop(0)
        
        if not self.cats:
            return self.dogs.pop(0)
        
        oldestDog = self.dogs[0]
        oldestCat = self.cats[0]

        if oldestCat.timestamp > oldestDog.timestamp:
            return self.cats.pop(0)
        else:
            return self.dogs.pop(0)
        
    def dequeueCat(self):
        if not self.cats:
            return None
        return self.cats.pop(0)
    
    def dequeueDog(self):
        if not self.dogs:
            return None
        return self.dogs.pop(0)
        

        


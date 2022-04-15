

from abc import ABC, abstractmethod


class LivingThing(ABC):
    
    @abstractmethod
    def sense():
        pass
    
    def detail():
        print("LivingThings")
        

class Human(LivingThing):
    
    def sense(self):
        print("Humans have 6 senses")
    
    def detail(self):
        print("This is Human")
        

h1 = Human()

print(h1)

# h1.sense()


        
    
    
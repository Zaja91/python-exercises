class Dog():

    def __init__(self, name, age): #viene invocato per ogni nuova instanza della classe
        """Initialize name and age attributes."""
        self.name = name #ogni var con self. e disponibile a ogni method nella classe
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

#Stacks = Last in first out in a list .append .pop
#Queues = first in first out from a list .append .popleft

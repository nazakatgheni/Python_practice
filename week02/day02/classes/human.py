from abc import ABC, abstractmethod

class Human(ABC):
    
    population = 0
    #dunder method in Pythons
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Human.population +=1 
        
    #? Common methods for all humans Behaver
    #eat
    #sleep
    #walk
    #run
    #communication
    
    def eat(self):
        print(f"{self.name} is eating")
        return True
    
    def sleep(self):
        print(f"{self.name} is sleeping")
        return True
    
    def walk(self):
        print(f"{self.name} is walking")
        return True
    
    def run(self):
        print(f"{self.name} is running")
        return True
    
    #Communicate method with optional parameters
    def communicate(self, message="Hello"):
        print(f"{self.name} says, '{message}'")
        
        
    #decorator
    @classmethod
    def get_population(cls):
        return(f"Total number of human: {cls.population}")
    
    @abstractmethod
    def work(self):
        pass
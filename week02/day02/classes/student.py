from classes.human import Human

#             inheritance
class Student(Human):
    #constructor
    def __init__(self, name, age, school):
        # thi super refer/reference to parent classes
        super().__init__(name,age)
        self.school =  school
        
    #Implementation or abstract method
    def work(self):
        print(f"{self.name}, the student, is studying at {self.school}")
    
    #Polymorphism - overloading an overriding
    #overloading
    def communicate(self, message="Hello", words="text"):
        if words == "text":
            print(f"{self.name}, the student, texts: '{message}'") 
        else:
            print(f"{self.name}, the student, says loudly: '{message}'") 
            
    # Additional method to student 
    def study(self):
        print(f"{self.name} is studying")
        
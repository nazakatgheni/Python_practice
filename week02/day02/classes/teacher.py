from classes.human import Human

class Teacher(Human):
    
    def __init__(self, name, age, school):
        # thi super refer/reference to parent classes
        super().__init__(name, age)
        self.school =  school
    
    #Implement
    def work(self):
        print(f"{self.name}, works in {self.school}")
    
    #Additional
    def work_hour(self):
        print(f"{self.name} is working 8h a day")
        
    #Poly
    def communicate(self, message="Hello", words="in_class"):
        if words == "in_class":
            print(f"{self.name}, the teacher announce: '{message}'") 
        else:
            print(f"{self.name}, the teacher whispers: '{message}'") 
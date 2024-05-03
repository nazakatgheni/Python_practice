from classes.student import Student
from classes.human import Human
from classes.teacher import Teacher

#Create a instance of Student class
amy = Student("Amy", 22, "GMU")

print(Human.get_population())

print("\nTesting student Class")

amy.eat()
amy.sleep()
amy.run()


tom = Teacher("Tom", 45, "GMU")
print(Human.get_population())
print("\nTesting Teacher Class")

tom.work()
tom.eat()
tom.walk()
tom.communicate("Hey, IT'S TIME TO GO BACK TO UR CLASS!!")
tom.communicate("Hey, wassup?")
#? if else statement
if 1 == 1:
    print("true")
else:
    print("not true")
    


age = 11
name = "Fred"
if age <= 12:
    print(f"{name} is a child")
elif age <=19:
    print(f"{name} is a teen")
else:
    print(f"{name} is an adult")
    
#? Module
# it does the division and return the remainder
line_number = 6
#print(line_number % 3)
if ( line_number % 2 == 0 ):
    print('Highlight the line')
else:
    print("Don't ~~~~")
    

#Write a Python program that classifies a given number into different categories.
# To classify the number into one of the following categories:
# If the number is even, print "The number [number] is even."
# If the number is odd, print "The number [number] is odd."
# If the number is zero, print "The number is zero."
# If the number is negative, print "The number [number] is negative."


#Mine
# x = 7
# if ( x < 0 ):
#     print(f"The number {x} is negative.")
# elif( x % 7 == 0 ):
#     print(f"The number {x} is even.")
# elif ( x % 7 == 1):
#     print(f"The number {x} is odd.") 
# else:
#     print(f"The number {x} is zero.")


# Maria
# number=-1
# if number == 0:
#         print("The number is zero.")
# elif number % 2 == 0:
#         print(f"The number {number} is even.")
# else:
#         print(f"The number {number} is odd.")
    
# if number < 0:
#         print(f"The number {number} is negative.")
        
        
#Bill
x = 10
if x == 0: 
    print("ZERO")
elif x > 0:
    if x % 2 ==0:
        print("EVEN")
    elif x % 2 == 1:
        print("ODD")
else: 
    print("NEGATIVE")
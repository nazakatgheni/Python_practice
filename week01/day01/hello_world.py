print("Hello WORLDDD")

#? 3 data type

#Strings
y=("hello!")
print(y)

#integer
y = 45
print(y)

#boolean
likes_chocolate = True

#? python syntax

x = 10

if x > 50:
    print("Bigger than 50")
else:
    print("Smaller than 50")

if x > 50:
    print("Bigger than 50")
else:
    pass #this means if its true/false just pass, === null

print(type(x)) # check data type

#? String Literal/Concatenation
first_name = "fred"
last_name = "Flinstone"

# using +
print(first_name + " " + last_name)

#comma after strings
full_name = first_name + " " + last_name
print("my name is", full_name)

#Type cast
total = 35
user_val = "26"

#total = total + user_val
#print(total) # this line will give us type error
# we use 
total = total + int(user_val)
print(total)
#? Convert a number or string to an integer, or return 0 if no arguments are given

total = str(total) + user_val
print(total)

#string interpolation
# f strings
print(f"My name is {first_name} {last_name}")


lower_case = "hello world"
print(lower_case.upper()) #HELLO WORLD
upper_case = "HELLO WORLD"
print(upper_case.lower()) #hello world

print(lower_case.count("o")) #2





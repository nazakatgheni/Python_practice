shopping_list  = ["marshmallows", "chocolate", "crackers"]

#access value
print(shopping_list[1]) # chocolate

shopping_list[2] = "pens"


#append - add new item onto the end of list
car_list = ["toyota", "Honda", "Lexus", "Ford"]
# car_list.append("MB")

# print(car_list)

#remove
# car_list.remove("Ford")
# print(car_list)


#delete
# del car_list[1]
# print(car_list)


#? Slicing in python
# Syntax [:]
# inclusive : exclusive (included vs not included)
# so it means before : is included but : after is not
print(car_list[1:])
print(car_list[1:3])

#length
#

# remove the end of the array
#

#mutable vs immutable
#? Tuples
my_tuple = (1, 2, "hello", True)

#access to value
print(my_tuple[2])
print(my_tuple[3])

# creating new tuple with updated elements/ values
new_tuple = my_tuple[:2] + ("world", ) + my_tuple[3:]
print(new_tuple)
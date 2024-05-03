price = 12

# if price < 10:
#     print("A")
# elif price > 15 and price <22:
#     print("B")
# elif price < 20:
#     print("C")
# elif int(price / 2) == 22:
#     print("D")
# elif price < 30 and price % 2 ==0:
#     print("E")
# elif price > 19:
#     print("F")
# else:
#     print("oops")
    
"""
    List 
        - mutable
        - can add/remove/update/rearrange elements
        - indexed
        - use: when you need to update elements
    
    Tuples
        - immutable
        - cannot add/remove/update/rearrange elements
        - indexed
        - use: when you want a fixed list that cannot be changed
"""
some_list = ["string","string"]
some_tuples = (1,2,"string", True)

#Dictionaries/Objects 
name = "Fred"
hair_color = "Brown"
age = 34

fred = {
#    key     value
    "name": "Fred",
    "hair_color": "Brown",
    "age": 34
}

nazuk = {
#    key     value
    "name": "Nazuk",
    "hair_color": "Green",
    "age": 22
}

print(nazuk["name"])

# Nested Dictionary
users_list = [
    {"name": "Nazuk","hair_color": "Green","age": 22, "is_student": True},  #0
    {"name": "Nazakat","hair_color": "Black","age": 22, "is_student": True}, #1
    {"name": "Maria","hair_color": "Black","age": 22, "is_student": True},   #2 
]
# print(users_list[0]["name"])
# print(users_list[1]["name"])
# print(users_list[2]["name"])
# print(users_list[2]["hair_color"])

# for i in range(len(users_list)):
#     print(users_list[i]["name"])
#     print(users_list[i]["is_student"])

# for each_person_list in users_list:
#     print(each_person_list["age"])

# for each_person_list in users_list:
#     for key in each_person_list.keys():
#         print(each_person_list[key])
        
user_1 = {"name": "Nazuk","hair_color": "Green","age": 22, "is_student": True, "email": ""}

# if "email" not in user_1:
#     user_1["email"] = "nazuk@email.com"
# else:
#     print("Would you like to update email?")
    # user_1["email"] = "nazuk@email.com"
    
# print(user_1)

#? Functions

def simple_function():
    print("Hello World")

# simple_function()

# Function with parameter
def display_message(message):
    print(message)
    
# display_message("Hell Maria")

# Function with default parameter and named parameter
def display_message(message, is_student=True):
    if(is_student):
        print(message.upper()) #uppercase
    else:
        print(message)

# display_message("hello world")
# display_message("hello world", False)

# return information
def do_calculation(num_1, num_2):
    return num_1 + num_2

result = do_calculation(5, 5)
print(result)
print(do_calculation(result, 11))
# print(do_calculation(25, 5))
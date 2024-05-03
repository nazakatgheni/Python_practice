#FOR LOOP

#with single argument
# for i in range(10):
#     print(i) # 0~9

#with two arguments
# print('two argument')
# for i in range(2,10):
#     print(i)
    
#with 3 arguments
# print('three argument')
# for i in range(2,16,3):
#     print(i)


# print("backwards")
# for i in range(10,2,-1):
#     print(i)

car_list = ["toyota", "Honda", "Lexus", "Ford"]

# for i in range(len(car_list)):
#     print(car_list[i])


# for each loop

# for i in car_list:
#     print(i)
    
for i in "string":
    if i == "i":
        print("This is", i)
    print(i)


#? While loop
# loop while  a certain condition is true

"""
    while condition is true
"""

count = 0
while count <= 5:
    print("Looping -", count)
    count+=2 # += means addition assignment 

# - given a list of numbers, return a new list with just the even numbers
# old_list = [3,6,8,9,2,5,6,0,1]
# new_list = []

# # your code goes here
# print(new_list)

old_list = [3,6,8,9,2,5,6,0,1]
new_list = []
for i in old_list:
    if i % 2== 0:
        new_list.append(i)
        print(new_list)
        
# old_list = [3,6,8,9,2,5,6,0,1]
# new_list = []
# while i % 2 == 0:
#     new_list.append(i)
#     print(new_list)
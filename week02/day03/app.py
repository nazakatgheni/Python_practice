# total = 0
# for i in range(1, 101):
#     total =+ i
# print(total) 

# squares_num = []
# for i in range(1, 21):
#     squares_num.append(i **2)
# print(squares_num)



# def even_list(n):
#     even_list = []
#     for i in range(2, n + 1):
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list
# n = 21
# even_num = even_list(n)
# print(even_num)
def score(num):
    if num >= 90:
        print("Excellent")
    elif 70 <= num <= 89:
        print("Good")
    elif 50 <= num <= 69:
        print("Average")
    else:
        print("False")
score(69)


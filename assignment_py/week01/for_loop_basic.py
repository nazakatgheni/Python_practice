
# Basic - Print all integers from 0 to 150.

for i in range(151):
    print(i)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
    print(i)


# 3. Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "TechCircle".
for i in range(0,101):
    if i % 10 == 0:
        print("TechCircle")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4. Add odd integers from 0 to 500,000, and print the final sum.
sum_of_odd = 0
for i in range(1, 500001, 2):
        sum_of_odd += i
print("sum of ood number is :", sum_of_odd)

# 5. Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
for i in range(2,9,3):
    print(i+1)
    

"""
    A simple calculator function that performs basic arithmetic operations.

    Args:
    operation (str): The operation to perform. It can be 'add', 'subtract', 'multiply', or 'divide'.
    x (int): The first number.
    y (int): The second number.

    Returns:
    float: The result of the arithmetic operation.
"""


def calculator(operation, x, y):
    pass


calculator("add", 5, 5)
calculator("divide", 10, 2)
calculator("subtract", 10, 2)
calculator("multiply", 11, 2)
calculator("random-word", 2, 2)




print("### Maria ###")
def calculator(operation,x,y):
    if operation.lower() == "add":
        return x+y
    elif operation.lower() =="subtract":
        return x-y
    elif operation.lower() =="multiply":
        return x*y
    elif operation.lower() =="divide":
        return x/y
    else:
        return "Invalid operation"
    
    
# print(calculator("add", 4, 4))
# print(calculator("subtract", 8, 4))
# print(calculator("multiply", 4, 4))
# print(calculator("divide", 16, 4))
# print(calculator("Subtract", 0, 4))
# print(calculator("ADD", 4, 4))


def calculator(operation, x, y):

    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operation!"
    
    

items = {
    "fruits": {
        "apples": {"quantity": 5},
        "bananas": {"quantity": 3},
        "oranges": {"quantity": 2}
    },
    "vegetables": {
        "carrots": {"quantity": 4},
        "potatoes": {"quantity": 6}
    }
}
# print("Bananas:",items["fruits"]["bananas"])
# print(items["vegetables"]["carrots"])

items["fruits"]["grapes"] = {"quantity": 10}

print(items)

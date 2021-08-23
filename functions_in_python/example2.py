def add():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print("Sum is: ", x + y)

def sub():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print("Difference is: ", x - y)

def mul():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print("Product is: ", x * y)

# but it is very bad way of coding, as taking input in function is not a good practice

# calling the function the correct way
if __name__ == '__main__':
    add()
    sub()
    mul()
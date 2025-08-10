print("Welcome to python calc")
print("enter first number: ")
a=int(input())
print("enter second number: ")
b=int(input())
def addition():
    return "The sum is: " + str(a + b)
def subtraction():
    return "The subtraction is: " + str(a - b)
def division():
    return "The division is: " + str(a / b)
def multiplication():
    return "The multiplication is: " + str(a * b)
switch ={ 
    1: addition,
    2: subtraction,
    3: division,
    4: multiplication
}
value = int(input("Enter 1 for addition,2 for subtraction,3 for division,4 for multiplication: "))
result=switch.get(value,lambda:"input proper function")()
print(result)
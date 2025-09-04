# calculator
def sum(a,b):
    return (a+b)
a= int(input("Enter first number: "))
#accepting input from user
b= int(input("Enter second number: "))
# print the variables and their sums
print (f'The sum of {a} and {b} is {sum(a,b)}')
def add(x,y): #addition function
    return (x+y)
def subract(x,y): #subtraction function
    return (x-y)
def multiply(x,y):#multiplication function
    return (x*y)
def divide(x,y):#division function
    if y!=0:
        return (x/y)
    else:
        return "Error! Can't divide by zero."
print("Select operation.")
print("1.Add")  
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(f"{num1} + {num2} = {add(num1,num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subract(num1,num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1,num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1,num2)}")
else:
    ("invalid input")
# Python functions
# They are a block of code/statements that performs given task/action. They can be reused throughout the program to perform different tasks. 
# Functions are defined using def keyword(def).
# We have two main types of functions i.e :
# 1. In-built functions -> They come pre installed with the interpretter i.e print() ,pop(), append() e.t.c..
# 2. User Defined Functions -> They are created by a programmer to solve a given task.That suits the entire programme.
# To define a function you need to give it a name followed by parenthesis
# For the functions , it is usually indented and to invoke a function we use the function name.


def greetings () :
    print("Hello! How are you?")

# Below we call the functionby use of its name
greetings()

print('======================')
# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the number is:" ,sum)


addition()    

print('======================')
# Create a function that is able to multiply three values
def multiplication():
    num1 = 3
    num2 = 4
    num3= 5
    product= num1 * num2 * num3 
    print("The product of the numbers is :", product)

multiplication()    

print('====================')
# Below is a division function
def divide():
    number1= int(input("Enter the first number:"))
    number2= int(input("Enter the second number:"))
    quotient= number1 / number2
    print("The answer is:",quotient)
    print('---------')
        

for function in range (3) :
    print("This is a new loop 1")
    divide()


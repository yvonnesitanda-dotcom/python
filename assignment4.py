# Create a function that takes no parameters , uses arithmetic operatos to calculate the area of a rectangle.
def rectanglearea():
    length = 5
    width = 2

    area = length * width
    print("The area of the rectangle is:",area)

rectanglearea()    

print('==========================')

# 2) Create a function that accepts two numbers as parameters and returns their sum , difference , product and division.
def arithmetical_operations(num1 , num2) :
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    division= num1 /num2
    return sum,difference,product,division


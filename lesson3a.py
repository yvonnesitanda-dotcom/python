# Boolean - This is a data type that evaluates to either truth or false

isRaining = False
print(isRaining)
print(type(isRaining))

paidLoan = True
print(paidLoan)
print(type(paidLoan))

# Comparison operators Thay are used to compare two or more statements and they usually return a boolean answer

number1 = 2
number2 = 5


print("is number1 greater than number 2", number1 > number2)
print("is number1 less than number 2", number1 < number2)
print("is number1 greater than or equal to number 2", number1 >= number2)
print("is number1 less than or equal to number 2", number1 <= number2)
print("is number1 equal to number 2", number1 == number2)
print("is number1 is not equal to number 2", number1 != number2)

# Logical operators
# Logical AND 
# It return true if and only if the condition/statements evaluate to true
print((3 > 1) and ( 7> 6))

# Logical or
# It evaluates to true if one of the statements/conditions is true
print(( 3 > 1) or (7 < 6))

# Logical not
# It is used to negate a statement/condition
print( not( 90 > 70))

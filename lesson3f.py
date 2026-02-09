# Create a python program that is able to determine whether a number entered is an odd number or an even number


# Create a python that is able to determine whether a person can donate blood based on the age and weight of a person . If the weight is greater that 50 kg and age is above 18 , then the person can donate blood , else not possible .

age = int (input ("Enter your age :"))
#print("The entered age is, age")

if age > 18 :
    print("Can donate")
else:
    print("Cannot donate donate")    

weight = int(input("Enter your weight :"))

if weight > 50 :
    print("Can donate")
else :
    print("Cannot donate")    
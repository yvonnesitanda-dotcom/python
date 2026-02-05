# A tubble is a immutable type of a list(it cannot change)
# To introduce a tuple , we use paranthesis ()


counties = ("Nairobi", " Mombassa" , " Nakuru" , "Eldoret" , "Kajiado" , "Kisii")

print(counties)
print(type(counties))

# slicing of tuples
print(counties[3:])

# accessing items of a tuple by use of the indexes
print(counties[5])

# Note: Below will generate an error
counties.append("Machakos")
print(counties)
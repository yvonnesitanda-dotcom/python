cities = [ "Nairobi" , "Kakamega" ," Mombasa" , "Eldoret", "Kisumu"]
search = input("Enter the name of the city")
found = False

for c in cities :
    if c == search :
        print (search, "is available")
        found = True
        break
if not found:
    print(search , "is not available")         
        
# A python for loop can also be used to iterate through a list, tuple , string or even a dictionary .
name = "Yvonne"

for letter in name :
    if letter == "n" :
         print("the letter is n")
        
    else:
         print(letter)

print('===============')
# Below is a list of counties
counties =[ "Nairobi " , "Mombasa" , "Kisumu " , "Nakuru" , "Eldoret" , "Kajiado" , "Machakos" , "Embu"]
print(counties)    

for county in counties :
     print(county)

print('===============')
for county in counties:
     if "Meru" in counties :
          print("Meru is in the list of counties")
          break
else :
     print("Meru county not found") 

print('====================')
#The for loop can be used to iterate through a dictionary  

player ={
     "name" : "Mbappe" ,
     "age" : 25 ,
     "team":["PSG", "Monacco","France"],
     "Nationality":"French"
}

for key in player :
     print(key)

     print('================')

for values in player :
     print(player [values])
#print(player["name"])

print('==========================')
# Loop through the teams the player has played for
for team in player ["team"] :
     print(team)
print('''
*******************************************************************************


       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
          / ||||| \
         /   \_/   \
        {}          {}

*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

cross_road = input("You've reached a crossroad. Would you like to go 'right' or 'left'? \n").lower()

if cross_road == 'right':
    print("You fell into a hole. Game over.")
elif cross_road == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input("Type 'wait' to wait for a boat or 'swim' to swim across:\n").lower()
    
    if action == 'wait':
        print("You arrived at the island unarmed.")
        door = input ("There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door == 'yellow':
          print ('You win')
        elif door == 'red':
          print ('Burned by fire. Game over')
        elif door == 'blue':
          print ('Eaten by beasts. Game Over.')
        else:
          print ('game over')
          
    elif action == 'swim':
        print("You tried to swim across the lake but got tired and drowned. Game over.")
    else:
        print("Invalid input. Game over.")
else:
    print("Fell into a hole. Game over.")

  









    

# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random

################ ALTERNATIVE SHORT CODE #######################

chosen_name = random.choice(names)

print (f'{chosen_name } is going to buy the meal today!')

################ ALTERNATIVE SHORT CODE #######################

len_names = len (names)

result_name = random.randint (0, len_names-1 )

# Use the random index to select a name
random_name = names[result_name]

print (f'{random_name } is going to buy the meal today!')


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


# Setting both names in lower cases for beter analysis

name1 = name1.lower()
name2 = name2.lower()


both_names = (name1 + name2) # setting a new variable 

##########################  count of each letter of the word 'true' in both names

count_t = both_names.count ('t')
count_r = both_names.count ('r')
count_u = both_names.count ('u')
count_e = both_names.count ('e')

count_true = (count_t + count_r + count_u + count_e)

##########################  count of each letter of the word 'love' in both names

count_l = both_names.count ('l')
count_o = both_names.count ('o')
count_v = both_names.count ('v')
count_e = both_names.count ('e')

count_love = (count_l + count_o + count_v + count_e)

###########################
score = str (count_true) + str (count_love)
love_score = int (score)

if love_score < 10 and love_score > 90:
    print (f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score > 40 and love_score < 50:
    print (f"Your score is {love_score}, you are alright together.")

else:
    print (f"Your score is {love_score}")







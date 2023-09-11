#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("Welcome to the tip calculator")

bill = float (input("Please enter the amount of your bill: "))

print()

number_people = int (input("Please enter the number of people: "))

print ()

tips_percent = float (input("Please enter the amount of tips in %: "))

print ()

tips = tips_percent / 100 * bill / number_people

each_pay_without_tips = round ((  bill / number_people  ), 2)
each_pay_with_tips =  round ( (( bill / number_people ) + tips) , 2 )

print ()
print ('-----------------------------------------------------')
print ()
print (f"Everyone will pay $ {each_pay_without_tips} + % {tips} dollars as tips so the total per each, including the tips will be: $ {each_pay_with_tips}")

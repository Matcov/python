# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

#*********************************************************************************************************#

# range() function gives range class in the output so we need to create a list out of the range classe in order to run for loop on it:

my_range = list (range (0,102,2) )

sum_result = 0
for number in my_range:
  sum_result += number
  
print (sum_result)

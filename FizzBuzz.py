# You are going to write a program that automatically prints the solution to the FizzBuzz game.

[WIKI] (https://en.wikipedia.org/wiki/Fizz_buzz)

# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

full_range = list (range(1, 101))

number = 0

for number in full_range:
    if (number % 3 == 0):
        print ('Fizz')
    elif (number % 5 == 0):
        print ('Buzz')
    elif (number % 3 == 0) and (number % 5 == 0):
        print ('FizzBuzz')
    else: 
        print (number)

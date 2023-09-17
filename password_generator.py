#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_number_inputs = nr_letters + nr_symbols + nr_numbers


print ('Total number of input symbols is: ', total_number_inputs)
print ()

random_numbers = random.sample(numbers, nr_numbers)
random_letters = random.sample (letters, nr_letters)
random_symbols = random.sample (symbols, nr_symbols)

randomly_concatenated_list = random_letters + random_numbers + random_symbols

password_list = random.sample (randomly_concatenated_list, total_number_inputs)

# Join the elements in the list into a single string without commas
password = ''.join(password_list)

print ('The generated password is: ', password)

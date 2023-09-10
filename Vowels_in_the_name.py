# Get the user's input
name = input('Please enter your name to know the number of vowels in it: ')


# Initialize a variable to count vowels
vowel_count = 0

# Define a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

# Iterate through each character in the name and check if it's a vowel
for letter in name:
    if letter in vowels:
        vowel_count = vowel_count + 1 # += 1

# Print the total number of vowels in the name
print(f 'The name "{name}" contains {vowel_count} vowels.')

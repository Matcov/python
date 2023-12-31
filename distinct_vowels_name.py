# Get the user's input and set it to lowercases, otherwise the result would not be in lowercases
name = input('Please enter your name or any other word or phrase \n to know the number distinct vowels it contains: ').lower()

# Initialize a variable to count vowels
vowel_count = 0

# Define a set to store the found vowels
found_vowels = set()

# Define a list of vowels
vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}

# Iterate through each character in the name and check if it's a vowel
for letter in name:
    if letter in vowels:
        vowel_count += 1
        found_vowels.add(letter)

# Create a temporary variable to to host the result of found vowels
temp = (", ".join(found_vowels))


# Split the string into a list using ',' as the delimiter
temp_list = temp.split(', ')

# Create a set from the list to remove duplicates
temp_set = set(temp_list)

# Count the number of entries in the set
entry_count = len(temp_set)

                
# print (entry_count)                

# Print the total number of vowels in the name and the distinct vowels
print(f'The name/word/phrase "{name}" contains {entry_count} distinct vowels: {", ".join(found_vowels)}')

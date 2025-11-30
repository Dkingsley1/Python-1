# Ask the user to enter a character

char = input ("Enter a single letter: ")

# Check length
if len(char) != 1:
    print("Error: Please enter exactly one character.")
    exit()

# Check that it's a letter
if not char.isalpha():
    print("Error: Input must be a letter.")
    exit()

# Check vowel or consonant
if not char.lower() in "aeiou":
    print("The character is a vowel.")
else:
    print("The character is a consonant.")
import random  # For generating random choices
import string  # For predefined sets of letters, digits, and punctuation
from colorama import Fore  # For colored text output in terminal

def generate_password():                            # Ask the user for the desired password length
    try:
        length = int(input(Fore.WHITE+"Enter the desired password length: ").strip())
        if length < 4:                              # Ensure the password is at least 4 characters long
            return Fore.RED+"The length of the password must be at least 4 characters!"+Fore.WHITE
    except ValueError:                              # Handle non-integer input
        return Fore.RED+"The input must be a digit!!!"+Fore.WHITE
    # Ask user if they want to include uppercase letters, digits, and special characters
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower().strip()
    include_digit = input("Include digits? (yes/no): ").lower().strip()
    include_special = input("Include special characters? (yes/no): ").lower().strip()
    
    # Define character sets
    lowercase = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if yes
    digit = string.digits if include_digit == "yes" else ""  # '0123456789' if yes
    special = string.punctuation if include_special == "yes" else ""  # '!@#$%^&*()_+...' if yes

    # Combine all allowed characters into one string
    all_characters = lowercase + uppercase + digit + special

    password = []
    # Ensure at least one character from each selected type is included
    if include_uppercase == "yes":
        password.append(random.choice(uppercase))
    if include_digit == "yes":
        password.append(random.choice(digit))
    if include_special == "yes":
        password.append(random.choice(special))
    
    # Fill the remaining password length with random characters from the allowed set
    remained_characters = length - len(password)
    for _ in range(remained_characters):
        password.append(random.choice(all_characters))
    random.shuffle(password)                            # Shuffle the list to avoid predictable order
    return Fore.GREEN+"".join(password)+Fore.WHITE      # Return the password as a string with green color

print("\n"+generate_password())                         # Run the password generator
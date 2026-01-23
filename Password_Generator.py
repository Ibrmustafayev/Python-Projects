import random
import string
from colorama import Fore

def generate_password():
    try:
        length = int(input(Fore.WHITE+"Enter the desired password length: ").strip())
        if length < 4:
            return Fore.RED+"The length of the password must be at least 4 characters!"+Fore.WHITE
    except ValueError:
        return Fore.RED+"The input must be a digit!!!"+Fore.WHITE
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower().strip()
    include_digit = input("Include digits? (yes/no): ").lower().strip()
    include_special = input("Include special characters? (yes/no): ").lower().strip()
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    digit = string.digits if include_digit == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    all_characters = lowercase + uppercase + digit + special

    password = []
    if include_uppercase == "yes":
        password.append(random.choice(uppercase))
    if include_digit == "yes":
        password.append(random.choice(digit))
    if include_special == "yes":
        password.append(random.choice(special))
    
    remained_characters = length - len(password)
    for _ in range(remained_characters):
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return Fore.GREEN+"".join(password)+Fore.WHITE

print("\n"+generate_password())
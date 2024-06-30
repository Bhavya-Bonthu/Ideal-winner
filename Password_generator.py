import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Define the character sets based on the options provided
    char_sets = ''
    if use_uppercase:
        char_sets += string.ascii_uppercase
    if use_lowercase:
        char_sets += string.ascii_lowercase
    if use_digits:
        char_sets += string.digits
    if use_special:
        char_sets += string.punctuation

    if not char_sets:
        raise ValueError("At least one character set must be selected")

    # Generate the password
    password = ''.join(random.choice(char_sets) for _ in range(length))
    return password

# Example usage:
password_length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
include_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
include_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

password = generate_password(password_length, include_uppercase, include_lowercase, include_digits, include_special)
print(f"Generated password: {password}")

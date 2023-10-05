import random
import string

def generate_password(length):
    # Define different character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on different lengths
    if length < 8:
        # For short passwords, use only lowercase letters and digits
        char_set = lower_case + digits
    elif length < 12:
        # For moderate size passwords, also use uppercase letters
        char_set = lower_case + upper_case + digits
    else:
        # For longer passwords, add special characters
        char_set = lower_case + upper_case + digits + special_chars

    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

# Get password length from user
try:
    password_length = int(input("Enter the desired password length: "))
    if password_length <= 0:
        raise ValueError("Password length should be a positive integer.")
except ValueError as e:
    print("Invalid input. Please enter a positive integer for password length.")
else:
    # Generate and Display the password
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

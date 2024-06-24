import random
import string

def password(length, uppercase, lowercase, digits, special_chars):
    """Generate a password based on the specified length and character types."""
    password_characters_set = ""
    
    # Add uppercase letters to the character set if selected
    if uppercase:
        password_characters_set += string.ascii_uppercase
    
    # Add lowercase letters to the character set if selected
    if lowercase:
        password_characters_set += string.ascii_lowercase
    
    # Add digits to the character set if selected
    if digits:
        password_characters_set += string.digits
    
    # Add special characters to the character set if selected
    if special_chars:
        password_characters_set += string.punctuation
    
    # Ensure at least one character type is selected
    if password_characters_set == "":
        print("Select at least one character type.")
        return None
    
    # Generate the password by randomly choosing characters from the selected set
    resultant_password = ''
    for i in range(length):
        resultant_password += random.choice(password_characters_set)
    
    return resultant_password

def main():
    """Main function to prompt user input and generate the password."""
    # Prompt the user to enter the length of the password
    length = int(input("Enter the desired length of the password: "))
    
    # Prompt the user to select character types
    uppercase_letters = input("1. Uppercase letters? (y/n): ").lower() == 'y'
    lowercase_letters = input("2. Lowercase letters? (y/n): ").lower() == 'y'
    digits = input("3. Digits? (y/n): ").lower() == 'y'
    special_characters = input("4. Special characters? (y/n): ").lower() == 'y'
    
    # Generate the password based on user preferences
    generated_password = password(length, uppercase_letters, lowercase_letters, digits, special_characters)
    
    # Display the generated password if it was successfully created
    if generated_password:
        print("The Generated Password:", generated_password)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()


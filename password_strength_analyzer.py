"""

Progam Title: Password Strength Analyzer (Course Project)
Version: 1.0
Author: Chidi Ozurumba
University: National University
Course: CYB 333 - Security Automation
Professor: Vincent Chapman
Date: 12/14/2025

"""

import string # Used for special characters

# List of common passwords
COMMON_PASSWORDS = ["password", "123456", "qwerty", "abc123","admin","administratr","password1","letmein"]

# Minimum password length

MIN_PASSWORD_LENGTH = 8

# Function to analyze password strength

def analyze_password(password):
    score = 100 # Start with a perfect score
    feedback = [] # Suggestions for improvement

    # Check password length
    if len(password) < MIN_PASSWORD_LENGTH:
        score -= 25
        feedback.append(f"Password is too short (minimium {MIN_PASSWORD_LENGTH} characters).")

    # Check for lowerase letters
    if not any(c.islower() for c in password):
        score -= 15
        feedback.append("Add lowercase letters.")

    # Check for uppercase letters
    if not any(c.isupper() for c in password):
        score -= 15
        feedback.append("Add uppercase letters.")

    # Check for numbers
    if not any(c.isdigit() for c in password):
        score -= 15
        feedback.append("Add numbers.")

    # Check for special characters
    if not any(c in string.punctuation for c in password):
        score -= 15
        feedback.append("Add special characters.")
    
    # Check if password is commonly used
    if password.lower() in COMMON_PASSWORDS:
        score -=30
        feedback.append("Password is too common.")


    return score, feedback

# Function to get user input
def get_password_input():
    
    while True:
        password = input("Enter a password to analyze: ").strip() # Remove leading/training spaces
        if not password:
            print("Error: Password cannot be empty. Please try again.")
        else:
            return password

# Main function

def main():

    password = get_password_input() # Get password input
    score, feedback = analyze_password(password) # Analyze the password

    # Display the score
    print("\nPassword Strength Score:", score, "/100")

    # Display suggestions if needed
    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print("-",item)
    else:
        print("Password is strong!")

    return

# Run the program
if __name__ == "__main__":
    main()
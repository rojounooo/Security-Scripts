# This script checks the strength of a password based on length, uppercase, lowercase, digits, and special characters.

# Password Policy:
# - Minimum length: 10 characters
# - At least one uppercase letter (A–Z)
# - At least one lowercase letter (a–z)
# - At least one digit (0–9)
# - At least one special character (@, #, $, %, ^, &, +, =, ., _, -)

# Import libraries
import re

# Display password policy
print("Password Policy:")
print("- At least 10 characters long")
print("- Contains at least one uppercase letter (A–Z)")
print("- Contains at least one lowercase letter (a–z)")
print("- Contains at least one digit (0–9)")
print("- Contains at least one special character: @ # $ % ^ & + = . _ -")
print()

# Input password
password = input("Enter a password to check its strength: ")

# Length check
if len(password) < 10:
    len_check = "Password is too short. It should be at least 10 characters long."
    len_pass = False
else:
    len_check = "Password length is sufficient."
    len_pass = True

# Uppercase check 
if not re.search("[A-Z]", password):
    case_check = "Password should contain at least one uppercase letter."
    case_pass = False
else:
    case_check = "Password contains uppercase letters."
    case_pass = True

# Lowercase check
if not re.search("[a-z]", password):
    lower_check = "Password should contain at least one lowercase letter."
    lower_pass = False
else:
    lower_check = "Password contains lowercase letters."
    lower_pass = True

# Digit check
if not re.search("[0-9]", password):
    digit_check = "Password should contain at least one digit."
    digit_pass = False
else:
    digit_check = "Password contains digits."
    digit_pass = True

# Symbol check
if not re.search("[@#$%^&+=._-]", password):
    symbol_check = "Password should contain at least one special character."
    symbol_pass = False
else:
    symbol_check = "Password contains special characters."
    symbol_pass = True

# Final output
print("\nPassword Strength Check Results:")
print(f"Length (≥10 chars):       {'✅' if len_pass else '❌'}")
print(f"Uppercase letters:         {'✅' if case_pass else '❌'}")
print(f"Lowercase letters:         {'✅' if lower_pass else '❌'}")
print(f"Digits:                    {'✅' if digit_pass else '❌'}")
print(f"Special characters:        {'✅' if symbol_pass else '❌'}")

# Overall strength

# Calculate password strength score
checks = [len_pass, case_pass, lower_pass, digit_pass, symbol_pass]
score = sum(checks)  # True counts as 1, False as 0

# Scoring interpretation
if score == 5:
    strength = "Very Strong"
elif score == 4:
    strength = "Strong"
elif score == 3:
    strength = "Moderate"
elif score == 2:
    strength = "Weak"
else:
    strength = "Very Weak"

# Final Output with Score
print(f"\nPassword Strength: {strength}")
if score < 5:
    print("Please consider strengthening your password by addressing the feedback above.")


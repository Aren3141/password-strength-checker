# main.py
import getpass # This is a module for secure password input
Password_Desired = False
password = getpass.getpass("Enter your password: ")

print("Choose a password between 8 and 15 characters.\n")

score = 0 #This is our variable with which we will calculate the password strength
while Password_Desired == False:
    if not password:
        print("❌ Password cannot be empty. Please try again.")
        password = getpass.getpass("Enter your password: ")
    else: 
        break
if 8 <= len(password) <= 15:
    print("✅ Length is acceptable")
    score += 1
else:
    print("❌ Password must be between 8 and 15 characters")

if any(char.isdigit() for char in password):
    print("✅ Contains a number")
    score += 1
else:
    print("❌ Must contain at least one number")

if any(char.isupper() for char in password):
    print("✅ Contains an uppercase letter")
    score += 1
else:
    print("❌ Must contain at least one uppercase letter")

if any(char.islower() for char in password):
    print("✅ Contains a lowercase letter")
    score += 1
else:
    print("❌ Must contain at least one lowercase letter")

if any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in password):
    print("✅ Contains a special character")
    score += 1
else:
    print("❌ Must contain at least one special character")

print("Password strength score:", score)

if score == 1:
    Random_password_request = ("Weak password, Would you like to generate a stronger password? (yes/no): ")
    if Random_password_request.lower() == "yes":
        print("Generating a stronger password...")
        import Random_Password_Generator
    else:
        print("Please try again with a stronger password.")
        Password_Desired = False

elif score == 2:
    print("Password is weak, consider improving it.")
    Random_password_request = input("Would you like to generate a stronger password? (yes/no): ")
    if Random_password_request.lower() == "yes":
        print("Generating a stronger password...")
        import Random_Password_Generator
    else:
        print("Please try again with a stronger password.")
        Password_Desired = False

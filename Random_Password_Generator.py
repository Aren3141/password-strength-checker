import random
import string #character set that ascii uses

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()" # This is the character set for the password
    return ''.join(random.choice(chars) for _ in range(length)) # The underscore is a placeholder, can be replaced with any variable name (maybe user can input later)

print("Suggested strong password:", generate_password())
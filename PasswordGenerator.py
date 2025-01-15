import random
import string

def generate_password(length):
    Characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ""
    
    for i in range(length):
        password += random.choice(Characters)
    
    return password

password_length = int(input("\n Enter the  password length: "))

generated_password = generate_password(password_length)

print(" Your generated password is:", generated_password)

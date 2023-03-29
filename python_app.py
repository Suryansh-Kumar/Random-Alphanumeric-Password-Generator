# Ask the user if they want otto generate the password or not
# If yes, ask for the password length
# generate a password
# print the password
# if initial response is no, exit the program

import string
import random

chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("Enter how long tou want your password to be: "))
    random.shuffle(chars)

    password = []
    for x in range(password_length):
        password.append(random.choice(chars))
    random.shuffle(password)
    password = "".join(password)
    print(password)

option  = input("Do you want to generate the password? (yes/no): ")
if option.lower() == "yes":
    generate_password()
elif option.lower() == "no":
    print("Program Ended!")
    quit()
else:
    print("Invalid Input, please input yes or no")
    quit()
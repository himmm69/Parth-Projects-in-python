


import random
import string  # Add this import

def password_generator(length = 10):
    alphabet = list(string.ascii_letters + string.digits)  
    password = []
    password = random.choices(alphabet,k = length)
    password_str = ''.join(password)
    print(password_str)
password_generator(2)

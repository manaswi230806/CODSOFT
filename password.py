import random
import string

print("===================================")
print("      PASSWORD GENERATOR 🔐")
print("===================================")

length = int(input("Enter length of password: "))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

password = ""
8
for i in range(length):
    random_char = random.choice(all_characters)
    password += random_char

print("\n===================================")
print(" Generated Password is :", password)
print("===================================")
print(" Strong Password Created Successfully ✅")
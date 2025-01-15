letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

import random

print("Welcome to the Password Generator!")

c_letters = int(input("How many letters would you like in your password?\n"))
c_numbers = int(input("How many numbers would you like?\n"))
c_symbols = int(input("How many symbols would you like?\n"))

password_list = []
for letter in letters:
    password_list.append(random.choice(letters))
    if len(password_list) == c_letters:
        break

for number in numbers:
    password_list.append(random.choice(numbers))
    if len(password_list) == c_letters + c_numbers:
        break

for symbol in symbols:
    password_list.append(random.choice(symbols))
    if len(password_list) == c_letters + c_numbers + c_symbols:
        break

random.shuffle(password_list)

password = ''
for character in password_list:
    password += character

print(f"Your new password is {password}!")


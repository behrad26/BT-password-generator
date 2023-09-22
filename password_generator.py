import sys
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits
ascii_chars = "!@#$%&"

print("Welcome to BT-password-generator!")
num, length = int(input("How many passwords do you want to generate? ")), int(input("How many characters do you want your password to have? "))
lowercase, uppercase = input("Do you want lowercase letters in your password? [Y/N] ").lower() == "y", input("Do you want uppercase letters in your password? [Y/N] ").lower() == "y"
numbers, special_chars = input("Do you want digits in your password? [Y/N] ").lower() == "y", input("Do you want special characters in your password? [Y/N] ").lower() == "y"

if not (num > 0 and length > 0 and (lowercase or uppercase or numbers or special_chars)):
    if not num > 0:
        print(f"Number of passwords ({num}) is not positive.")
    elif not length > 0:
        print(f"Length of passwords ({length}) is not positive")
    elif not (lowercase or uppercase or numbers or special_chars):
        print("Your password must contain: lowercase letters, uppercase letters, numbers or special characters")
    sys.exit(1)

chars = (lowercase * ascii_lowercase) + (uppercase * ascii_uppercase) + (numbers * digits) + (special_chars * ascii_chars)
generated = []
while len(generated) < num:
    string = ""
    for char in range(length):
        string += choice(chars)
    generated = list(set(generated + [string]))

print("\n".join(["Your password(s):"] + generated))
if input("Do you want to save passwords in a seperate file? [Y/N] ").lower() == "y":
    with open(input("Enter the file address including file extention (e.g. txt): "), "w") as file:
        file.write("\n".join(generated))
    print("Saved!")

print("Thanks for using BT-password-generator!")
import secrets
import string
import time
def header():
    print("=" * 50)
    print("PassForge".center(50))
    print("=" * 50)
    print("PASSWORD SECURITY TOOLKIT")
    print("Version 1.0")
    print("Developed by Ibrahim Abdulsobur")
    print("=" * 50)
header()
def menu():
    while True:
        print("[1] Password Generator")
        print("[2] Password strength checker")
        print("[0] Exit")
        ask_1 = int(input("Enter an option: "))
        if ask_1 == 1:
            characters =  string.ascii_letters + string.digits + string.punctuation
            length = int(input("Enter Password Length: "))
            password = ""
            for i in range(length):
                password += secrets.choice(characters)
            print(f"Generated Password: \033[32m{password}\033[0m")
########################################################################################################
        elif ask_1 == 2:
            ask_2 = input("Enter Password For strength Checking: ")
            score = 0
            #######################PASSWORD CHARACTERS######################
            # CHECK PASSWORD LENGTH
            if len(ask_2) >= 12:
                score += 1
                print("\033[32mLength requirement passed\033[0m")
            else:
                print("\033[31mPassword is shorter than 12 characters\033[0m")

            # CHECK UPPERCASE
            if ask_2 != ask_2.lower():
                score += 1
                print("\033[32mUppercase letter detected\033[0m")
            else:
                print("\033[31mNo uppercase letter detected\033[0m")
            # CHECK LOWERCASE
            if ask_2 != ask_2.upper():
                score += 1
                print("\033[32mLowercase Letter Deteceted")
            else:
                print("\033[31mLowercase not Detected")
            # CHECK SPECIAL CHARACTERS
            special_characters = "!@#$%^&*()_+=?><|/~"

            found_special = False

            for character in ask_2:
                if character in special_characters:
                    found_special = True
                    break

            if found_special:
                score += 1
                print("\033[32mSpecial character detected\033[0m")
            else:
                print("\033[31mNo special character detected\033[0m")

            # CHECK DIGITS
            found_digit = False

            for character in ask_2:
                if character.isdigit():
                    found_digit = True
                    break

            if found_digit:
                score += 1
                print("\033[32mNumber found in password\033[0m")
            else:
                print("\033[31mNo number found\033[0m")

            # PASSWORD SCORE
            print(f"\nPassword Score: {score}/5")

            if score <= 1:
                print("=" * 50)
                print("\033[31mPassword Strength: WEAK\033[0m")
                print("=" * 50)
            elif score <= 3:
                print("=" * 50)
                print("\033[33mPassword Strength: MEDIUM\033[0m")
                print("=" * 50)
            else:
                print("=" * 50)
                print("\033[32mPassword Strength: STRONG\033[0m")
                print("=" * 50)
        elif ask_1 == 0:
            break
        else:
            print("Invalid Option")
            break
menu()

import random
import string


def generate_password(length):
    # Characters jisse password banega
    characters = string.ascii_letters + string.digits + string.punctuation

    # Password generate
    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


# ---- main program ----
print("Password Generator")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length kam se kam 4 honi chaiye")
else:
    password = generate_password(length)
    print("Generated password:", password)

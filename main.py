import random
import string

def generate_password(words, symbols):
    while True:
        password = ""

        # Select a random word and ensure it meets the requirements
        word = random.choice(words)
        words_copy = words.copy()
        words_copy.remove(word)

        # Ensure each password includes the necessary character types
        lowercase = random.choice(string.ascii_lowercase)
        uppercase = random.choice(string.ascii_uppercase)
        number = random.choice(string.digits)
        symbol = random.choice(symbols)

        # Combine the word, number, and symbol with the required characters
        arr = [word, lowercase, uppercase, number, symbol]
        random.shuffle(arr)
        for e in arr:
            password += e

        # Add random characters to meet the minimum length requirement
        while len(password) < 12:
            password += random.choice(string.ascii_letters + string.digits + symbols)

        # Shuffle the password to ensure a random order
        password = ''.join(random.sample(password, len(password)))

        # Ensure the password is within the maximum length
        if 12 <= len(password) <= 30:
            # Capitalize the first letter if it's a character, lowercase the rest
            if password[0].isalpha():
                password = password[0].upper() + password[1:].lower()
            else:
                password = password[0] + password[1:].lower()

            # Print the word with the first letter capitalized and in lowercase
            if word.isalpha():
                print(word.capitalize())
                print(word.lower())
            
            return password

def main():
    words = ["the", "support", "team", "password", "does", "not", "comply", "with", "the", "corporate", "policy", "for", "privileged", "accounts"]
    symbols = "@$!%*?&"

    with open("generated_passwords.txt", "w") as file:
        for i in range(1000000):  # Adjusted count for a reasonable test
            password = generate_password(words, symbols)
            file.write(f"{password}\n")
            print(i)

    print("Passwords generated and saved to 'generated_passwords.txt'")

if __name__ == "__main__":
    main()
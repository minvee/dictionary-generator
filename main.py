import random
import string

def generate_password(words, symbols):
    while True:
        password = ""
        word = random.choice(words)
        words_copy = words.copy()
        words_copy.remove(word)

        symbol = random.choice(symbols)
        number = str(random.randint(0, 9999))

        # Ensure each password includes the necessary character types
        password += random.choice(string.ascii_lowercase)  # at least one lowercase
        password += random.choice(string.ascii_uppercase)  # at least one uppercase
        password += random.choice(string.digits)           # at least one number
        password += random.choice("@$!%*?&")               # at least one special character

        # Combine the word, number, and symbol with the required characters
        arr = [word, number, symbol]
        random.shuffle(arr)
        for e in arr:
            password += e

        # Add random characters to meet the minimum length requirement
        while len(password) < 12:
            password += random.choice(string.ascii_letters + string.digits + "@$!%*?&")

        # Shuffle the password to ensure a random order
        password = ''.join(random.sample(password, len(password)))

        # Ensure the password is within the maximum length
        if len(password) <= 30:
            # Capitalize the first letter if it's a character, lowercase the rest
            if password[0].isalpha():
                password = password[0].upper() + password[1:].lower()
            else:
                password = password[0] + password[1:].lower()
            
            # Print the word with the first letter capitalized and in lowercase
            if word.isalpha():
                print(f"Original word: {word.capitalize()}, Lowercase word: {word.lower()}")
            
            return password

def main():
    words = ["the", "support", "team", "password", "does", "not", "comply", "with", "the", "corporate", "policy", "for", "privileged", "accounts"]
    symbols = "@$!%*?&"

    with open("generated_passwords.txt", "w") as file:
        for i in range(250000):  # Adjusted count for a reasonable test
            password = generate_password(words, symbols)
            file.write(f"{password}\n")
            print(i)

    print("Passwords generated and saved to 'generated_passwords.txt'")

if __name__ == "__main__":
    main()

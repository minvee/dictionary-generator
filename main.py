import random
import string

def generate_password(words, symbols):
    while True:
        # Select a random word
        word = random.choice(words)
        
        # Ensure each password includes the necessary character types
        lowercase = random.choice(string.ascii_lowercase)
        uppercase = random.choice(string.ascii_uppercase)
        number = random.choice(string.digits)
        symbol = random.choice(symbols)

        # Prepare the base password components
        components = [word, lowercase, uppercase, number, symbol]
        
        # Add additional random characters to meet the minimum length requirement
        while len(''.join(components)) < 12:
            components.append(random.choice(string.ascii_letters + string.digits + symbols))
        
        # Shuffle only the non-word parts while keeping the word in place
        word_position = random.randint(0, len(components) - 1)
        non_word_parts = [c for c in components if c != word]
        random.shuffle(non_word_parts)
        components = non_word_parts[:word_position] + [word] + non_word_parts[word_position:]
        
        # Ensure the password is within the maximum length
        password = ''.join(components)
        if 12 <= len(password) <= 30:
            # Generate the capitalized and non-capitalized versions
            capitalized_word = word.capitalize()
            non_capitalized_word = word.lower()
            
            # Create two versions of the password
            password_with_capitalized_word = password.replace(word, capitalized_word, 1)
            password_without_word = password.replace(word, non_capitalized_word, 1)

            # Print both versions
            print(password_with_capitalized_word)
            print(password_without_word)
            
            # Save the password to the file
            return password_with_capitalized_word

def main():
    # The sentence in the secret message was: "The support team password does not comply with the corporate policy for privileged accounts!"
    # After removing the articles, auxiliary verbs, prepositions and adverbs from the sentence, left the following words:
    words = ["support", "team", "password", "comply", "corporate", "policy", "privileged", "accounts"]

    symbols = "@$!%*?&"

    with open("dictionary.txt", "w") as file:
        # Number of passwords in rockyou.txt is approximately 14,344,392
        for i in range(14350000):
            password = generate_password(words, symbols)
            file.write(f"{password}\n")

    print("Passwords generated and saved to 'dictionary.txt'")

if __name__ == "__main__":
    main()

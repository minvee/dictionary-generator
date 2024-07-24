import random
import string
import concurrent.futures

def generate_password(words, symbols):
    while True:
        # Select a random word
        word = random.choice(words)
        
        # Ensure each password includes the necessary character types
        components = [
            word,
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(symbols)
        ]
        
        # Add additional random characters to meet the minimum length requirement
        while len(components) < 12:
            components.append(random.choice(string.ascii_letters + string.digits + symbols))
        
        # Shuffle all parts
        random.shuffle(components)
        
        # Ensure the password is within the maximum length
        password = ''.join(components)
        if 12 <= len(password) <= 30:
            # Generate the capitalized and non-capitalized versions
            capitalized_word = word.capitalize()
            non_capitalized_word = word.lower()
            
            # Replace word with both versions
            password_with_capitalized_word = password.replace(word, capitalized_word, 1)
            password_without_word = password.replace(word, non_capitalized_word, 1)

            # Return both versions as a tuple
            return password_with_capitalized_word, password_without_word

def generate_and_save_passwords(words, symbols, num_passwords, file_path):
    with open(file_path, "w") as file:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = [executor.submit(generate_password, words, symbols) for _ in range(num_passwords)]
            for future in concurrent.futures.as_completed(futures):
                password_with_cap, password_without = future.result()
                file.write(f"{password_with_cap}\n")
                file.write(f"{password_without}\n")

def main():
    # The sentence in the secret message was: "The support team password does not comply with the corporate policy for privileged accounts!"
    # After removing the articles, auxiliary verbs, prepositions and adverbs from the sentence, left the following words:
    words = ["support", "team", "password", "comply", "corporate", "policy", "privileged", "accounts"]
    symbols = "@$!%*?&"
    
    # Number of passwords in rockyou.txt is approximately 14,344,392
    num_passwords = 14,350,000
    
    file_path = "dictionary.txt"

    generate_and_save_passwords(words, symbols, num_passwords, file_path)

    print("Passwords generated and saved to 'dictionary.txt'")

if __name__ == "__main__":
    main()
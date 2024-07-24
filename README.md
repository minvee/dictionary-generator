# Juice Shop Dictionary Generator
This project is a password generation script written in Python - specifically for Juice Shop: Login Support Team challenge. After finding the password requirements for support team and also the hidden message, the information gathered can be used to brute force the password to the KeePass file. This Python script creates passwords by combining a fixed set of words with random characters, ensuring each password meets specific security requirements.

The generated passwords are:
- **Length**: Between 12 and 30 characters.
- **Content**: Includes at least one lowercase letter, one uppercase letter, one digit, and one special character (@$!%*?&).
- **Word Placement**: Each password contains one of a predefined set of words, which remains intact and can be positioned anywhere in the password.

The script generates two versions of each password:
- With the selected word capitalized.
- With the selected word in lowercase.

Passwords are saved to **dictionary.txt**, with the goal of creating a comprehensive password list for security testing.

The script is designed to generate only 1 million passwords. This limitation helps prevent overwhelming the your device, in addition to the implementation of parallel processing. Note that it is only intended for testing purposes.

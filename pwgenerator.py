import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    if length <= 0:
        return "Invalid length. Must be greater than 0."

    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return "You must select at least one character type."

    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    print("Random Password Generator")
    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

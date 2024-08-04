def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? Enter 'E' or 'D': ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")
            continue

        message = input("Enter your message: ")
        try:
            shift = int(input("Enter shift value (0-25): "))
            if not (0 <= shift <= 25):
                raise ValueError
        except ValueError:
            print("Invalid shift value. Please enter a number between 0 and 25.")
            continue

        if choice == 'E':
            result = encrypt(message, shift)
        else:
            result = decrypt(message, shift)

        print(f"Result: {result}")

        another = input("Do you want to perform another operation? (Y/N): ").upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()

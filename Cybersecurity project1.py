from cryptography.fernet import Fernet
import hashlib
import base64

# Function to generate key from the password
def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Function to encrypt the file
def encrypt_file(file_path, password):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File encrypted and saved as {file_path}.enc")

# Function to decrypt the file
def decrypt_file(file_path, password):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_path.replace('.enc', '.dec'), 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        print(f"File decrypted and saved as {file_path.replace('.enc', '.dec')}")
    except Exception as e:
        print("Error: Incorrect password or corrupted file")

# Main program execution
if __name__ == "__main__":
    action = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip()
    file_path = input("Enter the file path: ").strip()
    password = input("Enter your password: ").strip()

    if action == 'encrypt':
        encrypt_file(file_path, password)
    elif action == 'decrypt':
        decrypt_file(file_path, password)
    else:
        print("Invalid action. Please enter 'encrypt' or 'decrypt'.")


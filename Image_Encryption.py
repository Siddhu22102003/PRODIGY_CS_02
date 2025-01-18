from PIL import Image
import os

def encrypt_image(image_path, key):
    """
    Encrypts an image by applying a XOR operation with the key to each pixel value.
    
    Args:
        image_path (str): Path to the input image.
        key (int): Encryption key (integer between 0 and 255).
    
    Returns:
        str: Path to the encrypted image.
    """
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure image is in RGB format
        pixels = img.load()

        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)  # XOR operation

        encrypted_path = "encrypted.png"  # Save as encrypted.png
        img.save(encrypted_path)
        return encrypted_path
    except Exception as e:
        print(f"Error encrypting image: {e}")
        return None


def decrypt_image(image_path, key):
    """
    Decrypts an image by reapplying the XOR operation with the same key.
    
    Args:
        image_path (str): Path to the encrypted image.
        key (int): Decryption key (same as the encryption key).
    
    Returns:
        str: Path to the decrypted image.
    """
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure image is in RGB format
        pixels = img.load()

        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)  # XOR operation

        decrypted_path = "decrypted.png"  # Save as decrypted.png
        img.save(decrypted_path)
        return decrypted_path
    except Exception as e:
        print(f"Error decrypting image: {e}")
        return None


def main():
    print("Welcome to the Image Encryption Tool!")
    while True:
        print("\nMenu:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")

        choice = input("Choose an option (1, 2, or 3): ")
        if choice == '1':
            image_path = input("Enter the path to the image to encrypt: ")
            if not os.path.exists(image_path):
                print("Error: File does not exist.")
                continue

            try:
                key = int(input("Enter an encryption key (integer between 0 and 255): "))
                if 0 <= key <= 255:
                    encrypted_path = encrypt_image(image_path, key)
                    if encrypted_path:
                        print(f"Image encrypted successfully! Saved as: {encrypted_path}")
                else:
                    print("Error: Key must be between 0 and 255.")
            except ValueError:
                print("Error: Invalid key. Please enter an integer.")

        elif choice == '2':
            image_path = input("Enter the path to the encrypted image: ")
            if not os.path.exists(image_path):
                print("Error: File does not exist.")
                continue

            try:
                key = int(input("Enter the decryption key (integer between 0 and 255): "))
                if 0 <= key <= 255:
                    decrypted_path = decrypt_image(image_path, key)
                    if decrypted_path:
                        print(f"Image decrypted successfully! Saved as: {decrypted_path}")
                else:
                    print("Error: Key must be between 0 and 255.")
            except ValueError:
                print("Error: Invalid key. Please enter an integer.")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

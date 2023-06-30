from ShieldCrypt.shieldcrypt import ShieldCrypt

def main():
    crypt = ShieldCrypt()

    # Generate a key and export it to a key file
    crypt.generate_key()
    crypt.export_key('key.key')

    # Import the key from a file if needed
    crypt.import_key('key.key')

    # Encrypt and decrypt data (runtime)
    plaintext = "This is a sample message."
    encrypted_data = crypt.encrypt(plaintext)
    decrypted_data = crypt.decrypt(encrypted_data)

    # Print the results
    print("Plaintext:", plaintext)
    print("Encrypted data:", encrypted_data)
    print("Decrypted data:", decrypted_data)

    # Encrypt and decrypt a file
    crypt.encrypt_file('test_file.txt', 'encrypted_file.txt')
    crypt.decrypt_file('encrypted_file.txt', 'decrypted_file.txt')

if __name__ == '__main__':
    main()

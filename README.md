# ShieldCrypt

ShieldCrypt is a powerful Python module for secure data encryption and decryption. It leverages the strength of AES (Advanced Encryption Standard) and advanced cryptographic algorithms to provide robust protection for sensitive information.

## Features

- Secure data encryption and decryption using AES.
- Key generation for encryption purposes.
- Customizable encryption modes to meet specific requirements.
- File encryption for secure storage and transmission.
- Ideal for secure file storage, communication, and password protection use cases.

## Installation

To install ShieldCrypt, simply use pip:

```shell
pip install shieldcrypt
```

## Usage

Here is an example of how to use ShieldCrypt for data encryption and decryption:

```python
from shieldcrypt import ShieldCrypt

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

```

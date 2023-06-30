# ShieldCrypt

ShieldCrypt is a powerful Python module for secure data encryption and decryption. It leverages the strength of AES (Advanced Encryption Standard) and advanced cryptographic algorithms to provide robust protection for sensitive information.

## Features

- Secure data encryption and decryption using AES.
- Key generation for encryption purposes.
- Customizable encryption modes to meet specific requirements.
- File encryption for secure storage and transmission.
- Ideal for secure file storage, communication, and password protection use cases.
- Emphasizes high code quality, documentation, and developer-friendly integration.

## Installation

To install ShieldCrypt, simply use pip:

```shell
pip install shieldcrypt
```

## Usage

Here is an example of how to use ShieldCrypt for data encryption and decryption:

```python
from shieldcrypt import ShieldCrypt

# Create a ShieldCrypt instance
crypt = ShieldCrypt()

# Generate a random encryption key
key = crypt.generate_key()

# Encrypt data
plaintext = "Sensitive information"
encrypted_data = crypt.encrypt(plaintext)

# Perform necessary operations with encrypted data

# Decrypt data
decrypted_data = crypt.decrypt(encrypted_data)
print(decrypted_data)  # Output: Sensitive information
```

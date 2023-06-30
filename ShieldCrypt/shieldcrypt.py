import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

class ShieldCrypt:
    def __init__(self, key=None):
        self.key = key or os.urandom(256)

    def encrypt(self, data):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(256).padder()
        padded_data = padder.update(data.encode()) + padder.finalize()

        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return iv + encrypted_data

    def decrypt(self, encrypted_data):
        iv = encrypted_data[:16]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()

        unpadder = padding.PKCS7(256).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        return unpadded_data.decode()

    def generate_key(self):
        self.key = os.urandom(32)

    def export_key(self, file_path):
        with open(file_path, 'wb') as file:
            file.write(self.key)

    def import_key(self, file_path):
        with open(file_path, 'rb') as file:
            self.key = file.read()

    def encrypt_file(self, file_path, encrypted_file_path):
        with open(file_path, 'rb') as file:
            data = file.read().decode()

        encrypted_data = self.encrypt(data)

        with open(encrypted_file_path, 'wb') as file:
            file.write(encrypted_data)
    def decrypt_file(self, encrypted_file_path, decrypted_file_path):
        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = self.decrypt(encrypted_data)

        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted_data.encode())
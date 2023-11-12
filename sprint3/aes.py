# Jiwon Park, Inigo Perez Gamiz

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def aes_encrypt(message, key):
    # Ensure the message is a multiple of the block size by adding PKCS7 padding
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message) + padder.finalize()

    # AES encryption implementation
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()

    return ciphertext

def aes_decrypt(ciphertext, key):
    # AES decryption implementation
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove PKCS7 padding
    unpadder = padding.PKCS7(128).unpadder()
    original_message = unpadder.update(decrypted_message) + unpadder.finalize()

    return original_message

def adjust_key_size(key):
    # Adjust key size to 256 bits
    n_bits = len(key)
    if n_bits < 256:
        adjusted_key = list(key)
        for i in range((256//n_bits) - 1):
            adjusted_key += key
        adjusted_key += key[:256-len(adjusted_key)]
    elif n_bits > 256:
        adjusted_key = key[0:256]
    else:
        adjusted_key = key
    return adjusted_key
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

str_to_encrypt = 'Hi, my name is Tomer Sagi';

# Key can be 16, 24, or 32 bytes
key = get_random_bytes(16)

# Create an AES cipher object
cipher = AES.new(key, AES.MODE_ECB)

# Data must be a multiple of 16 bytes
data = str_to_encrypt.encode()  # 16 characters -> 16 bytes

# Pad data to be a multiple of 16 bytes
padded_data = pad(data, AES.block_size)

# Encrypt
encrypted_data = cipher.encrypt(padded_data)
print("Encrypted (hex):", binascii.hexlify(encrypted_data))

# Decrypt
decrypted_padded_data = cipher.decrypt(encrypted_data)

# Unpad decrypted data to retrieve the original
decrypted_data = unpad(decrypted_padded_data, AES.block_size)
print("Decrypted:", decrypted_data.decode())
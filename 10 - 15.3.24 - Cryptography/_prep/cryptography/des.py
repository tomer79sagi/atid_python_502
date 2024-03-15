from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

# 1. String to encrypt
str_to_encrypt = 'Hi, my name is Tomer Sagi';

# 2. Key must be 8 bytes
key = get_random_bytes(8)

# 3. Create a DES cipher object
cipher = DES.new(key, DES.MODE_ECB)

# Encode the string to binary
data = str_to_encrypt.encode()  # 8 characters -> 8 bytes
print(f'data: {data}')

# Convert each byte to a string representation of the byte
# Use 8 bytes with leading 0s
str_bins = ' '.join([f'{byte:08b}' for byte in data])
print(str_bins)

# 4. Pad data to be a multiple of 16 bytes
padded_data = pad(data, DES.block_size)

# 5. Encrypt - Data must be a multiple of 8 bytes
encrypted_data = cipher.encrypt(padded_data)

print("Encrypted (hex):", binascii.hexlify(encrypted_data))

# 6. Decrypt
decrypted_padded_data = cipher.decrypt(encrypted_data)

# 7. Unpad decrypted data to retrieve the original
decrypted_data = unpad(decrypted_padded_data, DES.block_size)

# 8. Decode
print("Decrypted:", decrypted_data.decode())

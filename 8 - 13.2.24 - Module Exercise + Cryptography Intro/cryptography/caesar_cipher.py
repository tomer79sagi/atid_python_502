def encrypt(message, skip):
    encrypted_message = ''

    # 'a zoo', 3
    for char in message:
        if char.isalpha():  # Check if character is an alphabet
            # 'A' = 65, 'a' = 97
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start + skip) % 26
            new_ascii_code = start + offset
            encrypted_message = encrypted_message + chr(new_ascii_code)
            # 'a' --> (97 - 97 + 3) ==> 3 % 26 ==> 3 ==> 97 + 3 = 100 ==> 'd'
            # 'z' --> (122 - 97 + 3) ==> 28 % 26 ==> 2 ==> 97 + 2 = 99 ==> 'c'
        else:
            encrypted_message = encrypted_message + char

    return encrypted_message


original_message = 'Hello world'
encrypted_message = encrypt(original_message, 5)
print(original_message)
print(encrypted_message)


# Do Brute Force going backwards (because we know it's a Caesar cipher, i.e. skips forward)
# We can print the index going backwards and identify the 'skip' number
def hack_brute_force(message):
    for i in range(26, -1, -1):
        print(f'{i - 26} - {encrypt(message, i)}')


print('... Hacking ...')
hack_brute_force(encrypted_message)

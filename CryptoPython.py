from cryptography.fernet import Fernet

# Generating encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

choose = input("Do you want to crypt or decrypt text? (1 or 2)\n")
if choose == "1":
    # Asking user what do he want to crypt
    textocrypt = input("What do you want to crypt?\n")
    # Encoding to bytes
    cipher_text = cipher_suite.encrypt(textocrypt.encode())
    # Printing the encrypted message
    print("Your encrypted message is: {0}. While copying it, remove the quotes and the 'b'.".format(cipher_text))
    print("Your encryption key is:")
    # Printing the key
    print(key)
    print("It's EXTREMELY important that you keep it safe and send it ONLY to trusty people. When copying it, remove the quotes and the 'b'.")
else:
    # Asking user his encryption key
    key = input("What is your encryption key?\n")
    # Asking user to put his encrypted message here
    cipher_text = input("What is the message to decrypt ?\n")
    print("Your message is:")
    # Encoding the received key
    cipher_suite = Fernet(repr(key))
    # Decrypting message
    plain_text = cipher_suite.decrypt(cipher_text.encode())
    # Printing message
    print(plain_text)
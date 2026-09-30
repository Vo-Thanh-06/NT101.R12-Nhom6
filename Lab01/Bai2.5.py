def generate_key(text, key):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            result += key[key_index % len(key)]
            key_index += 1
        else:
            result += char
    return result

def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    full_key = generate_key(plaintext, key)
    ciphertext = ""
    for p, k in zip(plaintext, full_key):
        if p.isalpha():
            c = (ord(p) - 65 + ord(k) - 65) % 26
            ciphertext += chr(c + 65)
        else:
            ciphertext += p
    return ciphertext

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    full_key = generate_key(ciphertext, key)
    plaintext = ""
    for c, k in zip(ciphertext, full_key):
        if c.isalpha():
            p = (ord(c) - 65 - (ord(k) - 65) + 26) % 26
            plaintext += chr(p + 65)
        else:
            plaintext += c
    return plaintext

print("2.5 Vigenere Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Chon: ")

if choice == "1":
    plaintext = input("Nhap plaintext: ")
    key = input("Nhap khoa: ")
    print("Ban ma:", encrypt(plaintext, key))
elif choice == "2":
    ciphertext = input("Nhap ciphertext: ")
    key = input("Nhap khoa: ")
    print("Ban ro:", decrypt(ciphertext, key))
else:
    print("Lua chon khong hop le!")
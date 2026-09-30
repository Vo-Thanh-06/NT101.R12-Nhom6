def encrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            result += char
    return result
def decrypt(text, key):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            result += char
    return result

def brute_force(ciphertext):
    common_words = {
        'the', 'is', 'a', 'and', 'in', 'of', 'to', 'for',
        'with', 'on', 'at', 'by', 'an', 'this', 'it', 'under'
    }

    best_score = 0
    best_key = 0
    best_plaintext = ""

    for key in range(1, 26):
        decrypted = decrypt(ciphertext, key)
        clean_words = ''.join(
            c if c.isalpha() else ' ' for c in decrypted
        ).lower().split()
        score = sum(1 for word in clean_words if word in common_words)
        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = decrypted
    return best_key, best_plaintext

print(" 2.1 Ma hoa, giai ma va Brute Force Caesar Cipher ")
print("1. Encrypt")
print("2. Decrypt")
print("3. Brute Force")
choice = input("Chon: ")

if choice == "1":
    text = input("Nhap chuoi van ban goc: ")
    key = int(input("Nhap khoa: "))
    print("Ban ma hoa:", encrypt(text, key))

elif choice == "2":
    text = input("Nhap ban ma hoa: ")
    key = int(input("Nhap khoa: "))
    print("Chuoi van ban goc: ", decrypt(text, key))
elif choice == "3":
    ciphertext = input("Nhap ban ma: ")
    key, plaintext = brute_force(ciphertext)
    print("Khoa tim duoc:", key)
    print("Ban ro:", plaintext)
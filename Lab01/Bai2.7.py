def encrypt_rail_fence(text, key):
    if key <= 1:
        return text

    rails = [""] * key
    row = 0
    direction = 1

    for char in text:
        rails[row] += char

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return "".join(rails)


def decrypt_rail_fence(ciphertext, key):
    if key <= 1:
        return ciphertext

    rail = [["\n" for _ in range(len(ciphertext))]
            for _ in range(key)]

    row = 0
    direction = 1

    for col in range(len(ciphertext)):
        rail[row][col] = "*"

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    index = 0

    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == "*" and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    result = ""
    row = 0
    direction = 1

    for col in range(len(ciphertext)):
        result += rail[row][col]

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return result


while True:
    print("\nRAIL FENCE CIPHER")
    print("1. Encrypt")
    print("2. Decrypt")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        try:
            key = int(input("Enter key (number of rails): "))
        except ValueError:
            print("Invalid key!")
            continue

        if key < 2:
            print("Key must be at least 2!")
            continue

        plaintext = input("Enter plaintext: ")

        ciphertext = encrypt_rail_fence(plaintext, key)

        print("\nKey:", key)
        print("Plaintext:", plaintext)
        print("Ciphertext:", ciphertext)

    elif choice == "2":
        try:
            key = int(input("Enter key (number of rails): "))
        except ValueError:
            print("Invalid key!")
            continue

        if key < 2:
            print("Key must be at least 2!")
            continue

        ciphertext = input("Enter ciphertext: ")

        plaintext = decrypt_rail_fence(ciphertext, key)

        print("\nKey:", key)
        print("Ciphertext:", ciphertext)
        print("Decrypted text:", plaintext)

    elif choice == "0":
        print("Exit program.")
        break

    else:
        print("Invalid choice!")
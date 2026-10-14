from Crypto.Cipher import DES

def to_binary(data):
    return format(int.from_bytes(data, "big"), "064b")

def avalanche_test(key):
    plaintext1 = b"STAYHOME"
    plaintext2 = b"STAYHOMA"

    cipher1 = DES.new(key, DES.MODE_ECB)
    cipher2 = DES.new(key, DES.MODE_ECB)

    ciphertext1 = cipher1.encrypt(plaintext1)
    ciphertext2 = cipher2.encrypt(plaintext2)

    binary1 = to_binary(ciphertext1)
    binary2 = to_binary(ciphertext2)

    hamming_distance = sum(
        x != y
        for x, y in zip(binary1, binary2)
    )

    change_percentage = hamming_distance / 64 * 100

    print("\nDES Key:", key.decode())
    print("Plaintext 1:", plaintext1.decode())
    print("Plaintext 2:", plaintext2.decode())
    print("Ciphertext 1 (Hex):", ciphertext1.hex().upper())
    print("Ciphertext 2 (Hex):", ciphertext2.hex().upper())
    print("Ciphertext 1 (Binary):", binary1)
    print("Ciphertext 2 (Binary):", binary2)
    print("Hamming Distance:", hamming_distance, "bits")
    print(f"Bit Change Percentage: {change_percentage:.2f}%")

    return hamming_distance, change_percentage

key_list = [
    b"87654321",
    b"24521633",
    b"24521641",
    b"24521644"
]

for key in key_list:
    avalanche_test(key)

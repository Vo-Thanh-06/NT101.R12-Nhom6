
def F(right, subkey):
    return (right ^ subkey) & 0x0F


def feistel_round(L_in, R_in, subkey):
    L_out = R_in
    R_out = L_in ^ F(R_in, subkey)
    return L_out, R_out


def track_avalanche(msg, key):
    L = (msg >> 4) & 0x0F
    R = msg & 0x0F

    subkeys = [
        key & 0x0F,
        (key >> 4) & 0x0F,
        (key + 1) & 0x0F,
        (key + 2) & 0x0F
    ]

    states = [(L, R)]

    print(f"Khoi tao: L={L:04b}, R={R:04b}")

    for i in range(4):
        L, R = feistel_round(L, R, subkeys[i])
        states.append((L, R))
        print(f"Vong {i+1}: L={L:04b}, R={R:04b}")

    return states


print("--- Ma hoa M1 = 0xAA ---")
states1 = track_avalanche(0xAA, 0x12)

print("\n--- Ma hoa M2 = 0xAB ---")
states2 = track_avalanche(0xAB, 0x12)

print("\n--- So sanh so bit khac nhau ---")

for i in range(5):
    L1, R1 = states1[i]
    L2, R2 = states2[i]

    value1 = (L1 << 4) | R1
    value2 = (L2 << 4) | R2

    diff = bin(value1 ^ value2).count("1")
    print(f"Vong {i}: {diff} bit khac nhau ({diff / 8 * 100:.1f}%)")

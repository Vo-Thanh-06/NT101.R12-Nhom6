from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

SIZE = 16
BYTE_POS = 26       

def flip_bit(data, pos, bit=0):
    buf = bytearray(data)
    buf[pos - 1] ^= (1 << bit)
    return bytes(buf)

def damaged_blocks(a, b):
    return [k for k, i in enumerate(range(0, len(a), SIZE)) if a[i:i+SIZE] != b[i:i+SIZE]]

# Bước 1: tạo dữ liệu 1000 byte 
key = get_random_bytes(16)
iv = get_random_bytes(16)
message = pad(get_random_bytes(1000), SIZE)

configs = {
    "ECB": {"mode": AES.MODE_ECB},
    "CBC": {"mode": AES.MODE_CBC, "iv": iv},
    "CFB": {"mode": AES.MODE_CFB, "iv": iv, "segment_size": 128},
    "OFB": {"mode": AES.MODE_OFB, "iv": iv},
}

print(f"Số khối bản rõ: {len(message) // SIZE}\n")
for name, params in configs.items():
    # Bước 2: mã hóa AES-128
    cipher_text = AES.new(key, **params).encrypt(message) 
    # Bước 3: đảo 1 bit tại byte thứ 26  
    broken = flip_bit(cipher_text, BYTE_POS)  
    # Bước 4: giải mã bản mã lỗi             
    result = AES.new(key, **params).decrypt(broken)        
    bad = damaged_blocks(message, result)
    print(f"{name}: {len(bad)} khối lỗi, vị trí {bad} , (khối 0 là khối đầu tiên)")
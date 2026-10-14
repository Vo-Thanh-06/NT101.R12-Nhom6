
from Crypto.Cipher import AES

key = b"1234567890123456"
plaintext = b"UIT_LAB_UIT_LAB_UIT_LAB_UIT_LAB_"
iv = b"1234567890123456"

cipher_ecb = AES.new(key, AES.MODE_ECB)
ct_ecb = cipher_ecb.encrypt(plaintext)

cipher_cbc = AES.new(key, AES.MODE_CBC, iv=iv)
ct_cbc = cipher_cbc.encrypt(plaintext)

cipher_cfb = AES.new(key, AES.MODE_CFB, iv=iv)
ct_cfb = cipher_cfb.encrypt(plaintext)

cipher_ofb = AES.new(key, AES.MODE_OFB, iv=iv)
ct_ofb = cipher_ofb.encrypt(plaintext)

cipher_ctr = AES.new(key, AES.MODE_CTR)
ct_ctr = cipher_ctr.encrypt(plaintext)
print("ECB:", ct_ecb.hex())
print("CBC:", ct_cbc.hex())
print("CFB:", ct_cfb.hex())
print("OFB:", ct_ofb.hex())
print("CTR:", ct_ctr.hex())

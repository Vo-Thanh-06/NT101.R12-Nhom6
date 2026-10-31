import hashlib
with open("ca_modulus.txt", "r") as f:
    n_str = f.read().strip().replace("Modulus=", "")
    n = int(n_str, 16)
with open("ca_exponent.txt", "r") as f:
    e_str = f.read().strip()
    e = int(e_str.split("(")[0].split(":")[-1].strip())

with open("cert_signature.hex", "r") as f:
    sig_hex = f.read().strip()
    S = int(sig_hex, 16)

EM_int = pow(S, e, n)

key_byte_length = (n.bit_length() + 7) // 8
EM_bytes = EM_int.to_bytes(key_byte_length, byteorder='big')
EM_hex = EM_bytes.hex()

sha256_prefix = "3031300d060960864801650304020105000420"
if sha256_prefix in EM_hex:
    extracted_hash = EM_hex.split(sha256_prefix)[-1][:64]
else:
    extracted_hash = EM_hex[-64:]

with open("c0_body.bin", "rb") as f:
    body_data = f.read()

computed_hash = hashlib.sha256(body_data).hexdigest()

print("=" * 65)
print("XÁC MINH THỦ CÔNG CHỨNG CHỈ X.509 RSA")
print("=" * 65)
print(f"[+] Băm SHA-256 giải mã từ Chữ ký CA : {extracted_hash}")
print(f"[+] Băm SHA-256 tính từ tệp c0_body.bin   : {computed_hash}")
print("-" * 65)

if extracted_hash.lower() == computed_hash.lower():
    print("KẾT QUẢ: CHỨNG CHỈ HỢP LỆ (Chữ ký CA khớp hoàn toàn)")
else:
    print("KẾT QUẢ: CHỨNG CHỈ KHÔNG HỢP LỆ")
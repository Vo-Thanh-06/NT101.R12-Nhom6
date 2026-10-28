import hashlib

msg1_hex = "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"
msg2_hex = "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70"

b1 = bytes.fromhex(msg1_hex)
b2 = bytes.fromhex(msg2_hex)

diff = sum(1 for x, y in zip(b1, b2) if x != y)
md5_1 = hashlib.md5(b1).hexdigest()
md5_2 = hashlib.md5(b2).hexdigest()

is_same = "CO" if md5_1 == md5_2 else "KHONG"

print(f"So byte khac biet giua hai thong diep: {diff}")
print(f"MD5 Message 1: {md5_1}")
print(f"MD5 Message 2: {md5_2}")
print(f"Cac gia tri MD5 nay co giong nhau hay khong?: {is_same}")

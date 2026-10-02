import string
from collections import Counter

alphabet = string.ascii_uppercase

trigrams = {
"THE":5.0,"AND":4.5,"ING":4.3,"ENT":4.0,"ION":3.8,
"HER":3.5,"FOR":3.4,"THA":3.3,"NTH":3.2,"INT":3.1,
"ERE":3.0,"TIO":2.9,"TER":2.8,"EST":2.7,"ERS":2.6,
"ATI":2.5,"HAT":2.4,"ATE":2.3,"ALL":2.2,"ETH":2.1
}

english_freq = {
'E':12.7,'T':9.1,'A':8.2,'O':7.5,'I':7.0,'N':6.7,
'S':6.3,'H':6.1,'R':6.0,'D':4.3,'L':4.0,'C':2.8,
'U':2.8,'M':2.4,'W':2.4,'F':2.2,'G':2.0,'Y':2.0,
'P':1.9,'B':1.5,'V':1.0,'K':0.8,'X':0.2,'J':0.15,
'Q':0.1,'Z':0.07
}


def clean_text(text):
    return ''.join(c for c in text.upper() if c.isalpha())


def index_of_coincidence(text):
    N = len(text)
    freq = Counter(text)
    ic =0
    for f in freq.values():
        ic += f*(f-1)
    return ic/(N*(N-1)) if N>1 else 0


def kasiski(cipher):
    seq_pos = {}
    for i in range(len(cipher)-3):
        seq = cipher[i:i+3]
        if seq not in seq_pos:
            seq_pos[seq] = []
        seq_pos[seq].append(i)
    distances = []
    for seq in seq_pos:
        pos = seq_pos[seq]
        if len(pos) > 1:
            for i in range(len(pos)-1):
                distances.append(pos[i+1]-pos[i])
    factors = []
    for d in distances:
        for i in range(2,21):
            if d%i == 0:
                factors.append(i)
    return Counter(factors).most_common(10)


def guess_key_lengths(cipher):
    kasiski_result = kasiski(cipher)
    candidates = [k[0] for k in kasiski_result]
    if not candidates:
        candidates = list(range(2,11))
    ic_scores = {}
    for k in candidates:
        ic_sum = 0
        for i in range(k):
            group = cipher[i::k]
            ic_sum += index_of_coincidence(group)
        ic_scores[k] = ic_sum/k
    sorted_keys = sorted(ic_scores.items(), key = lambda x:abs(0.065-x[1]))
    return [k[0] for k in sorted_keys]


def chi_square(text):
    N = len(text)
    freq = Counter(text)
    score = 0
    for c in alphabet:
        observed = freq.get(c,0)
        expected = english_freq[c]*N/100
        if expected>0:
            score += (observed-expected)**2/expected
    return score


def break_caesar(group):
    best_shift = 0
    best_score = float("inf")
    for shift in range(26):
        decrypted = ""
        for c in group:
            p = (ord(c)-65-shift)%26
            decrypted += chr(p+65)
        score = chi_square(decrypted)
        if score<best_score:
            best_score = score
            best_shift = shift
    return best_shift


def find_key(cipher,key_len):
    key = ""
    for i in range(key_len):
        group = cipher[i::key_len]
        shift = break_caesar(group)
        key += chr(shift+65)
    return key


def decrypt(cipher,key):
    plaintext = ""
    for i,c in enumerate(cipher):
        shift = ord(key[i%len(key)])-65
        p = (ord(c)-65-shift)%26
        plaintext += chr(p+65)
    return plaintext


def trigram_score(text):
    score = 0
    for i in range(len(text)-2):
        tri = text[i:i+3]
        if tri in trigrams:
            score += trigrams[tri]
    return score


def break_vigenere(cipher):
    key_lengths = guess_key_lengths(cipher)
    best_key = ""
    best_plain = ""
    best_score = -1
    for klen in key_lengths[:5]:
        key = find_key(cipher, klen)
        plain = decrypt(cipher, key)
        score = trigram_score(plain)
        if score > best_score:
            best_score = score
            best_key = key
            best_plain = plain
    return best_key, best_plain


def main():
    while True:
        print("\n1. Nhap ciphertext")
        print("2. Doc file")
        print("3. Thoat")
        mode = input("Lua chon: ")
        if mode == "3":
            print("Dang thoat chuong trinh...")
            break
        elif mode == "2":
            filename = input("Nhap ten file: ")
            try:
                with open(filename,"r",encoding="utf-8") as f:
                    text = f.read()
            except:
                print("Khong the mo file.")
                continue
        elif mode == "1":
            text = input("Nhap ciphertext:\n")
        else:
            print("Lua chon khong hop le.")
            continue
        cipher = clean_text(text)
        print("\nDo dai ciphertext:", len(cipher))
        print("\nDang phan tich...\n")
        key,plain = break_vigenere(cipher)
        print("Khoa:",key)
        print("\nBan plaintext sau khi giai ma:\n")
        print(plain)
if __name__=="__main__":
    main()
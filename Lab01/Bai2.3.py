import random
import re
import string
import time
from collections import Counter

# 1. DỮ LIỆU THỐNG KÊ TIẾNG ANH

ENG_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
COMMON_WORDS = {
    "THE", "AND", "OF", "TO", "A", "IN", "IS", "THAT", "IT", "WAS",
    "FOR", "ON", "ARE", "WITH", "AS", "BE", "AT", "ONE", "HAVE",
    "THIS", "FROM", "OR", "HAD", "BY", "BUT", "WHAT", "SOME", "WE",
    "CAN", "OUT", "OTHER", "WERE", "ALL", "THERE", "WHEN", "UP",
    "YOUR", "HOW", "AN", "EACH", "SHE", "WHICH", "DO", "THEIR",
    "TIME", "IF", "WILL", "WAY", "ABOUT", "MANY", "THEN", "THEM",
    "WOULD", "WHO", "MORE", "HAS", "HE", "NOT"
}
COMMON_BIGRAMS = {
    "TH", "HE", "IN", "ER", "AN", "RE", "ON", "AT", "EN", "ND",
    "TI", "ES", "OR", "TE", "OF", "ED", "IS", "IT", "AL", "AR",
    "ST", "TO", "NT", "NG", "SE", "HA", "AS", "OU", "IO", "LE"
}
COMMON_TRIGRAMS = {
    "THE", "AND", "ING", "HER", "ERE", "ENT", "THA", "NTH",
    "WAS", "FOR", "HAT", "ION", "TIO", "VER", "EST", "ERS",
    "ATI", "HIS", "ALL", "ITH"
}
# 2. CHẤM ĐIỂM PLAINTEXT 

def calculate_fitness(text):
    text = text.upper()
    score = 0
    words = re.findall(r"[A-Z]+", text)
    for word in words:
        if word in COMMON_WORDS:
            score += len(word) * 50
    letters = re.sub(r"[^A-Z]", "", text)
    for i in range(len(letters) - 1):
        if letters[i:i + 2] in COMMON_BIGRAMS:
            score += 10
    for i in range(len(letters) - 2):
        if letters[i:i + 3] in COMMON_TRIGRAMS:
            score += 30
    return score

# 3. TẠO KHÓA BAN ĐẦU BẰNG PHÂN TÍCH TẦN SUẤT

def create_initial_key(ciphertext):
    letters = re.sub(r"[^A-Z]", "", ciphertext.upper())
    counts = Counter(letters)
    sorted_chars = [
        char for char, count in counts.most_common()
    ]
    for char in string.ascii_uppercase:
        if char not in sorted_chars:
            sorted_chars.append(char)
    return dict(zip(sorted_chars, ENG_FREQ))

# 4. GIẢI MÃ THEO KHÓA HIỆN TẠI 

def decrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += key.get(char, char)
        elif char.islower():
            result += key.get(char.upper(), char.upper()).lower()
        else:
            result += char
    return result

# 5. HOÁN ĐỔI HAI KÝ TỰ TRONG KHÓA 

def swap_key(key):
    new_key = key.copy()
    c1, c2 = random.sample(
        list(new_key.keys()), 2
    )
    new_key[c1], new_key[c2] = (
        new_key[c2],
        new_key[c1]
    )
    return new_key

# 6. GIẢI MÃ TỰ ĐỘNG BẰNG HILL CLIMBING 

def solve_cipher(ciphertext):
    initial_key = create_initial_key(ciphertext)
    best_key = initial_key.copy()
    best_text = decrypt(ciphertext, best_key)
    best_score = calculate_fitness(best_text)
    restarts = 15
    max_iterations = 5000
    for restart in range(restarts):
        current_key = initial_key.copy()
        # Tạo điểm bắt đầu khác cho mỗi lần chạy
        if restart > 0:
            for _ in range(10):
                current_key = swap_key(current_key)
        current_text = decrypt(ciphertext, current_key)
        current_score = calculate_fitness(current_text)
        no_improve = 0
        for _ in range(max_iterations):
            new_key = swap_key(current_key)
            new_text = decrypt(ciphertext, new_key)
            new_score = calculate_fitness(new_text)
            # Chỉ giữ khóa mới nếu kết quả tốt hơn
            if new_score > current_score:
                current_key = new_key
                current_score = new_score
                no_improve = 0
            else:
                no_improve += 1
            # Dừng sớm nếu không còn cải thiện
            if no_improve >= 700:
                break
        if current_score > best_score:
            best_key = current_key.copy()
            best_score = current_score
            best_text = decrypt(ciphertext, best_key)
    return best_text, best_key

# 7. NHẬP CIPHERTEXT 

def input_ciphertext():
    print("=== GIẢI MÃ MONO-ALPHABETIC SUBSTITUTION ===")
    print("1. Nhập ciphertext trực tiếp")
    print("2. Đọc ciphertext từ file")
    choice = input("Chọn: ")
    if choice == "1":
        print("\nNhập ciphertext, gõ DONE ở dòng riêng để kết thúc:")
        lines = []
        while True:
            line = input()
            if line.strip() == "DONE":
                break
            lines.append(line)
        return "\n".join(lines)
    elif choice == "2":
        path = input("\nNhập đường dẫn file: ").strip('"')
        try:
            with open(path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as error:
            print("Không đọc được file:", error)
            return None
    else:
        print("Lựa chọn không hợp lệ.")
        return None
# 8. CHƯƠNG TRÌNH CHÍNH

def main():
    ciphertext = input_ciphertext()
    if not ciphertext:
        print("Ciphertext rỗng.")
        return

    print("\nĐang giải mã, vui lòng chờ vài giây...")
    start_time = time.time()
    plaintext, key = solve_cipher(ciphertext)
    end_time = time.time()
    print("\n========== KẾT QUẢ ==========\n")
    print(plaintext)
    print("\nKhóa tìm được:")
    print(
        "Cipher:",
        string.ascii_uppercase
    )
    print(
        "Plain :",
        "".join(
            key[c]
            for c in string.ascii_uppercase
        )
    )
    print(
        f"\nThời gian xử lý: "
        f"{end_time - start_time:.2f} giây"
    )

if __name__ == "__main__":
    main()

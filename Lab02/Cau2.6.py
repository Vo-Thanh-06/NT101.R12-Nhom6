import random

def is_prime(n, k=40):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def random_prime(bits):
    if bits < 2:
        raise ValueError("So bit phai lon hon hoac bang 2")
    while True:
        num = random.getrandbits(bits)
        num |= (1 << (bits - 1)) | 1
        if is_prime(num):
            return num


def largest_primes_below_mersenne():
    M = 2**89 - 1
    primes = []
    n = M - 2
    while len(primes) < 10 and n > 1:
        if is_prime(n):
            primes.append(n)
        n -= 2
    return primes


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def mod_exp(base, exp, mod):
    if mod <= 0:
        raise ValueError("So modulo phai lon hon 0")
    if exp < 0:
        raise ValueError("So mu phai lon hon hoac bang 0")
    result = 1 % mod
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def main():
    M = 2**89 - 1
    print("1.1 SINH SO NGUYEN TO")
    print("So nguyen to 8 bit :", random_prime(8))
    print("So nguyen to 16 bit:", random_prime(16))
    print("So nguyen to 64 bit:", random_prime(64))
    print("\n1.2 TIM 10 SO NGUYEN TO LON NHAT NHO HON MERSENNE")
    print("So nguyen to Mersenne thu 10:", M)
    primes = largest_primes_below_mersenne()
    for i, prime in enumerate(primes, 1):
        print(f"{i}. {prime}")
    print("\n1.3 KIEM TRA SO NGUYEN TO")
    num = int(input("Nhap so can kiem tra: "))
    if num >= M:
        print("So nhap vao phai nho hon 2^89 - 1")
    elif is_prime(num):
        print(num, "la so nguyen to")
    else:
        print(num, "khong phai la so nguyen to")
    print("\n2. TINH UOC CHUNG LON NHAT")
    a = int(input("Nhap so a: "))
    b = int(input("Nhap so b: "))
    print(f"UCLN({a}, {b}) = {gcd(a, b)}")
    print("\n3. TINH LUY THUA MODULO")
    base = int(input("Nhap co so a: "))
    exp = int(input("Nhap so mu x: "))
    mod = int(input("Nhap modulo p: "))
    try:
        result = mod_exp(base, exp, mod)
        print(f"{base} ^ {exp} mod {mod} = {result}")
    except ValueError as e:
        print("Loi:", e)


if __name__ == "__main__":
    main()
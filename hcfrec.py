def gcd(a, b):
    if a == 0 :
        return b
    a, b = max(a, b), min(a, b)
    return gcd(a%b, b)

print(gcd(5, 6))
def digitalSum(n):
    if n < 10:
        return n
    return n % 10 + digitalSum(n // 10)
# def gcd(a, b):
#     if b == 0: return a
#     return gcd(b, a % b)
# print(gcd(20, 12))

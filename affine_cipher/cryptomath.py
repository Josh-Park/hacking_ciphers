
# Uses Euclidean algorithm to get greatest common denominator of two numbers
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def find_mod_inverse(a, m):
    # Returns the modular inverse of a % m
    # Defined as number x such that (a * x) % m = 1
    if gcd(a, m) != 1:
        return None # No mod inverse if a and m aren't relatively prime

    # Uses extended Euclidean algorithm to calculate
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m
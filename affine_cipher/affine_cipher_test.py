import affine_cipher
import cryptomath

message = "Make things as simple as possible, but not simpler."
for key_a in range(2, 80):
    key = key_a * len(affine_cipher.SYMBOLS) + 1

    if cryptomath.gcd(key_a, len(affine_cipher.SYMBOLS)) == 1:
        print(key_a, affine_cipher.encrypt_message(key, message))
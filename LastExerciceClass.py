import random

# Paramètres pour le chiffrement ElGamal
p = 71398895185373183
g = 123457
A = 57037618745651077
vote = 1
msg = 2**vote

#b = 9753462813963
b = 9753462814963
B = pow(g, b, p)
print(f"B: {B}")

K = pow(A, b, p)
print(f"K: {K}")

C = (msg * K) % p
print(f"C: {C}")

test = (pow(A,-b,p)*C)%p
print(f"Test: {test}")
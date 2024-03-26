def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Paramètres
p = 23 # Nombre premier
g = 5  # Générateur
x = 4  # Clé privée
y = pow(g, x, p) # Clé publique

# Signature d'un message m
m = 8
k = 3 # Doit être choisi aléatoirement, mais pour l'exemple, nous prenons 3
while gcd(k, p-1) != 1:
    k += 1

r = pow(g, k, p)
s = (modinv(k, p-1) * (m - x * r)) % (p-1)

# Vérification de la signature
v1 = pow(g, m, p)
v2 = (pow(y, r, p) * pow(r, s, p)) % p

# Affiche le résultat de la vérification
print("Signature valide:", v1 == v2)

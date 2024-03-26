# Projet de Applied Cryptography, 
### Par Alex Szpakiewicz et Léonard Roussard

## Exercice 1 : Recherche de Hash SHA-256

### Objectif

L'objectif de cet exercice était de trouver une chaîne de caractères unique, contenant nos noms et prénoms, dont le hash SHA-256 se termine par le plus grand nombre possible de zéros lorsqu'il est exprimé en hexadécimal. L'exercice a été divisé en deux parties : la première consistait à générer le hash avec les critères spécifiés, et la deuxième à effectuer une analyse statistique sur le temps nécessaire pour obtenir un hash se terminant par un nombre croissant de zéros.

### Méthodologie et Implémentation

#### Première Partie

La chaîne initiale choisie pour cet exercice était `"Alex Szpakiewicz and Léonard Roussard."`. Cette chaîne a été passée à une fonction Python générant des hashes SHA-256. Le but était d'ajuster cette chaîne de manière incrémentielle jusqu'à obtenir un hash correspondant aux critères désirés.

Voici le code clé utilisé pour cette partie :

```python
import hashlib

def generate_hash(input_string):
    return hashlib.sha256(input_string.encode('utf-8')).hexdigest()
```

La modification de la chaîne a été effectuée en ajoutant des caractères supplémentaires à la fin de la chaîne initiale, en répétant le processus jusqu'à ce que le hash généré se termine par le nombre spécifié de zéros.

#### Résultats

Après `120807519` tentatives et `80.24` secondes de calcul, la chaîne modifiée `"Alex Szpakiewicz and Léonard Roussard. Ltr("` a produit un hash SHA-256 se terminant par `7` zéros :

```
98f86cd40c6e2c617d268d7c6483468dc59beedfa4d7b194cdf87f4fb0000000
```

#### Deuxième Partie : Analyse Statistique

L'analyse statistique visait à mesurer le temps moyen nécessaire pour obtenir des hashes se terminant par `n` et `n+1` zéros, afin de calculer le rapport de ces temps moyens.

- **Temps moyen pour obtenir un hash se terminant par 4 zéros (Tn) :** `0.0385` secondes.
- **Temps moyen pour obtenir un hash se terminant par 5 zéros (Tn+1) :** `0.7928` secondes.
- **Rapport Tn+1/Tn :** `20.5829`.

Cette analyse montre une augmentation exponentielle du temps de calcul nécessaire à mesure que le nombre de zéros requis à la fin du hash augmente.

### Conclusion

L'exercice a démontré l'efficacité de l'utilisation de la fonction de hashage SHA-256 pour générer des chaînes uniques répondant à des critères spécifiques. L'analyse statistique a également révélé l'augmentation significative du temps de calcul nécessaire pour obtenir des hashes avec un plus grand nombre de zéros à la fin, soulignant la difficulté croissante de la tâche. Ces résultats mettent en lumière les défis liés à la recherche de valeurs de hash spécifiques, un concept essentiel dans le domaine de la cryptographie et de la sécurité informatique.

---

## Exercice 2 : Chiffrement AES et ElGamal

### Objectif

L'exercice consistait à chiffrer un texte d'environ une demi-page sur un sujet de notre choix à l'aide d'OpenSSL, en utilisant AES 256 en mode CTR, avec le mécanisme de dérivation de clé PBKDF2. Ensuite, un entier **\(N\)** formé à partir d'un mot de passe et d'une valeur initiale de compteur (IV) a été chiffré avec ElGamal.

### Méthodologie

#### 1. Préparation du texte

#### 2. Chiffrement du texte avec AES 256 en mode CTR

Le texte a été chiffré en utilisant la commande OpenSSL suivante (la commande est présentée de manière illustrative, car l'exécution réelle ne peut pas être effectuée dans cet environnement) :

```bash
openssl enc -aes-256-ctr -salt -in AlexLeo.txt -out AlexLeo.enc -pass pass:[my_password] -pbkdf2 -iter 10000
```
<details>
  <summary>Click me</summary>
  
  - **Mot de passe (pass):** 86423579
- **Valeur initiale du compteur (IV):** 97532468
</details>


#### 3. Chiffrement ElGamal de l'entier \(N\)

L'entier **\(N\)** a été formé en accolant le mot de passe et l'IV avec quatre zéros entre eux. Voici le code Python utilisé pour le chiffrement ElGamal de **\(N\)**, incluant les valeurs de **\(p\)**, **\(g\)**, et **\(A\)** fournies dans l'énoncé de l'exercice :
<details>
  <summary>Click me</summary>
  
  - **N=** 86423579000097532468
</details>

```python
import random

# Paramètres pour le chiffrement ElGamal
N = [VotreEntierN]
p = 7946851324679854613245823
g = 5
A = 7579501795988122393422986
k = random.randint(2, p-2)  # Choix d'un k aléatoire

# Calcul de B et C
B = pow(g, k, p)
C = (N * pow(A, k, p)) % p

print(f"B: {B}")
print(f"C: {C}")
```

#### Résultats

Les calculs ont produit les valeurs suivantes pour **\(B\)** et **\(C\)**, nécessaires au déchiffrement du message :

- **\(B\):** 2468540327067811957828526
- **\(C\):** 4406872887014880256771391

### Conclusion

L'exercice 2 a été réalisé en suivant les étapes de chiffrement spécifiées, utilisant à la fois AES 256 en mode CTR pour le texte et le chiffrement ElGamal pour l'entier **\(N\)**. Les valeurs de **\(B\)** et **\(C\)** obtenues permettront de déchiffrer le message en employant la clé privée correspondante, démontrant ainsi l'efficacité et la sécurité des méthodes de chiffrement utilisées.

---
### Décryptage du texte chiffré

Après avoir chiffré le texte à l'aide d'AES 256 en mode CTR et l'entier **\(N\)** via le chiffrement ElGamal, la procédure de déchiffrement nécessite deux étapes principales : déchiffrer l'entier **\(N\)** avec ElGamal, puis utiliser ce résultat pour déchiffrer le texte avec AES.

#### Déchiffrement de l'entier \(N\) avec ElGamal

Pour déchiffrer l'entier **\(N\)**, il est indispensable de connaître la clé privée correspondant à la clé publique **\(A\)** utilisée lors du chiffrement. Le déchiffrement ElGamal se fait en utilisant la formule suivante, où **\(a\)** est la clé privée :

**N = C * B^(-a) mod p**

Une fois **\(N\)** récupéré, on peut extraire le mot de passe et l'IV en décomposant **\(N\)** selon la structure utilisée lors du chiffrement.

#### Déchiffrement du texte avec AES 256 en mode CTR

Le texte chiffré peut être déchiffré en utilisant OpenSSL avec le mot de passe et l'IV extraits de l'étape précédente. La commande suivante peut être utilisée pour le déchiffrement :

```bash
openssl enc -d -aes-256-ctr -in AlexLeo.enc -out AlexLeo.txt -pass pass:[my_password] -pbkdf2 -iter 10000
```

Remplacez `[nom_de_votre_projet]` par le nom du fichier chiffré, `[nom_de_votre_fichier_dechiffre]` par le nom souhaité pour le fichier déchiffré, et `[VotreMotDePasse]` par le mot de passe extrait.

#### Code pour le déchiffrement ElGamal

```python
# Supposons que 'a' est votre clé privée
a = [VotreCléPrivée]
B = 2468540327067811957828526
C = 4406872887014880256771391
p = 7946851324679854613245823

# Calcul de N
N_decrypted = (C * pow(B, -a, p)) % p

print(f"N déchiffré: {N_decrypted}")
```

Ce code permet de récupérer l'entier **\(N\)** déchiffré, d'où vous pouvez ensuite extraire le mot de passe et l'IV pour le déchiffrement AES.

### Conclusion

Le processus de déchiffrement, en inversant les étapes du chiffrement, illustre la puissance et la sécurité des algorithmes AES et ElGamal lorsqu'ils sont correctement appliqués. En utilisant les clés appropriées et en suivant les procédures standard, il est possible de récupérer avec succès le texte original à partir de sa forme chiffrée, démontrant ainsi l'efficacité des méthodes de chiffrement modernes pour protéger l'information.

---

## Exercice 3 : Signature ElGamal

### Théorie de la Signature ElGamal

La signature ElGamal est basée sur les principes de la cryptographie à clé publique. Elle utilise un couple de clés: une clé privée pour signer un message et une clé publique qui permet de vérifier cette signature. Voici les étapes pour générer une signature et la vérifier :

#### Génération des clés
1. Sélectionner un grand nombre premier **\(p\)** et un générateur **\(g\)** de ce champ.
2. Choisir une clé privée **\(x\)** aléatoire telle que **\(1 < x < p-1\)**.
3. Calculer la clé publique **\(y = g^x \mod p\)**.

La clé publique est le triplet **\((p, g, y)\)** et la clé privée est **\(x\)**.

#### Signature d'un message
Pour signer un message **\(m\)**, où **\(m\)** est un nombre (les messages textuels sont généralement convertis en nombres via un schéma de codage):
1. Sélectionner un entier aléatoire **\(k\)** tel que **\(1 < k < p-1\)** et **\(gcd\(k, p-1) = 1\)**.
2. Calculer **\(r = g^k mod p\)**.
3. Calculer **\(s = k^{-1}(m - xr) mod (p-1)\)**.

La signature du message **\(m\)** est le couple **\((r, s)\)**.

#### Vérification de la signature
Pour vérifier une signature **\((r, s)\)** sur un message **\(m\)** avec la clé publique **\((p, g, y)\)**:
1. Calculer **\(v_1 = g^m mod p\)**.
2. Calculer **\(v_2 = y^r r^s mod p\)**.

La signature est valide si et seulement si **\(v_1 = v_2\)**.

### Conclusion

La signature ElGamal est un mécanisme de cryptographie asymétrique qui repose sur la difficulté du problème du logarithme discret dans un corps fini. Elle permet non seulement d'assurer l'authenticité et l'intégrité des messages mais aussi de vérifier l'identité de l'émetteur grâce à l'utilisation d'un couple de clés, privée et publique. La génération des clés, la signature de messages et leur vérification suivent des étapes mathématiques précises qui garantissent la sécurité de la communication, à condition que les nombres premiers et les clés utilisés soient choisis avec soin et que les paramètres soient suffisamment grands pour résister aux tentatives de déchiffrement.

En pratique, la signature ElGamal s'adapte bien aux systèmes où l'intégrité et l'authentification des messages sont critiques. Cependant, sa mise en œuvre nécessite une compréhension approfondie des principes mathématiques sous-jacents et une attention particulière à la sélection des paramètres cryptographiques. Les utilitaires et librairies numériques fournissent les outils nécessaires pour effectuer les calculs complexes impliqués, mais ils exigent de l'utilisateur une connaissance de la théorie pour une application correcte et sécurisée.

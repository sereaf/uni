#!/usr/bin/env python
# coding: utf-8

# 1. Lagrange\-interpoláció segítségével valósítsd meg a **Shamir**\-féle titokmegosztást! A megoldáshoz használható a **lagrange\_polynomial** parancs.  
# 
# 

# In[ ]:


def generate_shares(secret, k, n, prime):
    from random import randint
    coefficients = [secret] + [randint(1, prime - 1) for _ in range(k - 1)]
    shares = [(i, sum(coeff * (i**exp) for exp, coeff in enumerate(coefficients)) % prime) for i in range(1, n + 1)]
    return shares

def reconstruct_secret(shares, prime):
    R = PolynomialRing(GF(prime), 'x')
    x = R.gen()
    lagrange_poly = sum(
        y * prod((x - xj) / (xi - xj) for xj, _ in shares if xj != xi)
        for xi, y in shares
    )
    return lagrange_poly(0)

secret = 1234
k = 3
n = 5
prime = 1613

shares = generate_shares(secret, k, n, prime)
for share in shares:
    print(f"x = {int(share[0])}, y = {int(share[1])}")

subset = shares[:k]
recovered_secret = reconstruct_secret(subset, prime)
print(recovered_secret)


# 2. Írj osztályt, amely megvalósítja az ismétléses kódolást az alábbi váznak megfelelően!  
# 
# 

# In[ ]:


class RepCode:
    def __init__(self, k):
        self.__k = k

    def encode(self, data):
        encoded_data = []
        for symbol in data:
            encoded_data.extend([symbol] * self.__k)
        return encoded_data

    def decode(self, cdata):  # only notify about errors
        n = self.__k
        errors_detected = False
        decoded_data = []
        for i in range(0, len(cdata), n):
            chunk = cdata[i:i + n]
            if chunk.count(chunk[0]) != n:
                errors_detected = True
            decoded_data.append(chunk[0])
        if errors_detected:
            print("Errors detected")
        else:
            print("No errors detected.")
        return decoded_data

    def decode_with_correction(self, cdata):  # if there are errors, try to correct them
        n = self.__k
        corrected_data = []
        for i in range(0, len(cdata), n):
            chunk = cdata[i:i + n]
            corrected_symbol = max(set(chunk), key=chunk.count)
            corrected_data.append(corrected_symbol)
        return corrected_data


# 3. Írj programot, amely két bináris kódszó esetén meghatározza azok Hamming\-távolságát!  
# 
# 

# In[ ]:


def hd(u,v):
    return sum(c1 != c2 for c1, c2 in zip(u, v))
u = '011'
v = '010'
assert 1 == hd(u,v)


# 4. Írj programot, amely egy, a kódszavak halmazával megadott bináris kód Hamming\-távolságát határozza meg!  
# 
# 

# In[ ]:


def min_hamming_distance(codewords):
    n = len(codewords)
    min_distance = len(codewords[0])
    for i in range(n):
        for j in range(i + 1, n):
            distance = sum(c1 != c2 for c1, c2 in zip(codewords[i], codewords[j]))
            if distance < min_distance:
                min_distance = distance
    return min_distance

codewords = ['000', '011', '101', '110']
min_distance = min_hamming_distance(codewords)
print(min_distance)


# 5. Írj programot, amely a bemenetnek megfelelően meghatározza egy bináris kódszó vagy egy bináris kód \(kódhalmazzal adott\) Hamming\-súlyát!  
# 
# ​
# 

# In[ ]:


def hamming_weight(code):
    if isinstance(code, str):
        return code.count('1')
    elif isinstance(code, list):
        return [word.count('1') for word in code]

u = '1011'
print(hamming_weight(u))

codewords = ['0000', '1100', '1010', '1001']
weights = hamming_weight(codewords)
for word, weight in zip(codewords, weights):
    print(f"'{word}': {weight}")


# 6. Írj programot, amely a egy egyenletes kódhoz tartozó kódhalmaz alapján elkészíti a dekódolási táblázatot minimális súlyú dekódoláshoz egy **dict** formájában!  
# 
# 

# In[ ]:


def error_correcting_table(C):
    from itertools import product
    n = len(next(iter(C)))
    all_words = [''.join(bits) for bits in product('01', repeat=n)]
    decoding_table = {}
    for word in all_words:
        min_distance = n + 1
        closest_codeword = None
        for codeword in C:
            distance = sum(b1 != b2 for b1, b2 in zip(word, codeword))
            if distance < min_distance:
                min_distance = distance
                closest_codeword = codeword
        decoding_table[word] = closest_codeword
    return decoding_table

C = {'00000', '00111', '11001', '11110'}
print(error_correcting_table(C))


# 

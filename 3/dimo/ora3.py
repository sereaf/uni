# Prímekkel kapcsolatos fogalmak ellenörzése:
print("Is -1 a unit ", ZZ(-1).is_unit())
print("Is 2 unit in integer ring? ", ZZ(2).is_unit())
print("Is 2 unit in rational field? ", QQ(2).is_unit())
print("Is 6 irreducible? ", ZZ(6).is_irreducible())
print("Is -7 irreducible? ", ZZ(-7).is_irreducible())
print("Is 4 a prime? ", is_prime(4))
print("Is 7 a prime? ", ZZ(7).is_prime())
print("Is 7 a prime? ", 7 in Primes())



# Néhány prímekkel kapcsolatos SageMath eljárás:
print("First prime following 1000: ", next_prime(1000))
print("Largest prime below 1000: ", previous_prime(1000))
print("First 20 prime: ", primes_first_n(20))
print("Primes between 10 and 20: ", [p for p in primes(10,20)])
print("135th prime: ", nth_prime(135))



primes_first_n(10)
nth_prime(10)

N = 10
numbers = list(range(2, nth_prime(N)+1))

def eratos(l, i):
    if i >= len(l):
        return l
    k = l[i]
    return eratos([n for n in l if n == k or n % k != 0], i+1)
    
    
eratos(numbers, 0)

N = 10
numbers = [n for n in range(2, nth_prime(N)+1) if n == 2 or n % 2 != 0]

def eratos(l, i):
    if i >= len(l):
        return l
    k = l[i]
    return eratos([n for n in l if n == k or n % k != 0], i+1)
    
    
eratos(numbers, 0)





# a factor parancs megadja a kanonikus alakot
a = -829406174141952
F = factor(a)
print("Canonical form of", a, ":             ", F)
print("Unit parti of", a, ":                 ", F.unit())
print("Prime divisors of", a, ":             ", [t[0] for t in F])
print("Prime divisors with powers for", a, ":", [t for t in F])
print("The result of the factor command is a factorization object:", type(F))

N1 = 56
N2 = 28
print(gcd(N1, N2))

af = factor(N1)
bf = factor(N2)
GCM = {}
a_primes = [prime for prime, exp in af]
b_primes = [prime for prime, exp in bf]
com_primes = set([prime for prime in a_primes+b_primes if prime in a_primes and prime in b_primes])

GCD = {}
for f in [af, bf]:
    for prime, exp in f:
        if prime in com_primes:
            if prime in GCD:
                GCD[prime] = min(GCD[prime], exp)
            else:
                GCD[prime] = exp
            
n = 1
for k, v in GCD.items():
    n *= k^v
n

N1 = 28
N2 = 56
print(lcm(N1, N2))

factors = [factor(f) for f in [N1, N2]]
LCM = {}
for f in factors:
    for prime, exp in f:
        if prime in LCM:
            LCM[prime] = max(LCM[prime], exp)
        else:
            LCM[prime] = exp
            
n = 1
for k, v in LCM.items():
    n *= k^v
n

import time

def gcd_w_factor(a,b):
    af = factor(a)
    bf = factor(b)
    GCM = {}
    a_primes = [prime for prime, exp in af]
    b_primes = [prime for prime, exp in bf]
    com_primes = set([prime for prime in a_primes+b_primes if prime in a_primes and prime in b_primes])

    GCD = {}
    for f in [af, bf]:
        for prime, exp in f:
            if prime in com_primes:
                if prime in GCD:
                    GCD[prime] = min(GCD[prime], exp)
                else:
                    GCD[prime] = exp

    n = 1
    for k, v in GCD.items():
        n *= k^v
    return n

def gcd_w_eukl(a,b):
    if b == 0:
        return a
    return gcd_w_eukl(b, a % b)


data = []
for i in range(5,20+1):
    runtime_of_euc_gcd = 0
    runtime_of_fac_gcd = 0
    for j in range(10):
        a = randint(10^i,10^(i+1))
        b = randint(10^i,10^(i+1))
        c = gcd(a,b)
        start = time.time()
        assert gcd_w_eukl(a,b) == c
        runtime_of_euc_gcd += time.time() - start
        start = time.time()
        assert gcd_w_factor(a,b) == c
        runtime_of_fac_gcd += time.time() - start
    runtime_of_euc_gcd /= 10
    runtime_of_fac_gcd /= 10
    data.append([i,runtime_of_euc_gcd,runtime_of_fac_gcd])

plot1 = point([(d[0],d[1]) for d in data],color="red", legend_label="Eucl")
plot2 = point([(d[0],d[2]) for d in data], legend_label="Factor")
show(plot1+plot2)

def binary_gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    
    shift = 0
    while (a | b) & 1 == 0:
        a >>= 1
        b >>= 1
        shift += 1
       
    while a & 1 == 0:
        a >>= 1

    while b != 0:
        while b & 1 == 0:
            b >>= 1
    
        if a > b:
            a, b = b, a
        b = b - a
        
    return a << shift

print(gcd(48, 28))
print(binary_gcd(48, 28))

def gcd_extended(a, b):        
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

print(xgcd(25, 12))
print(gcd_extended(25, 12))

def binary_xgcd(a, b):
    if a == 0:
        return b, 0, 1
    elif b == 0:
        return a, 1, 0
    
    shift = 0
    while (a | b) & 1 == 0:
        a >>= 1
        b >>= 1
        shift += 1
        
    u, v = a, b
    u_coeff, v_coeff = 1, 0
    u_coeff_b, v_coeff_b = 0, 1
    
    while u != 0 and v != 0:
        while u & 1 == 0:
            u >>= 1
            if u_coeff & 1 == 0 and v_coeff & 1 == 0:
                u_coeff >>= 1
                v_coeff >>= 1
            else:
                u_coeff = (u_coeff + b) >> 1
                v_coeff = (v_coeff - a) >> 1

        while v & 1 == 0:
            v >>= 1
            if u_coeff_b & 1 == 0 and v_coeff_b & 1 == 0:
                u_coeff_b >>= 1
                v_coeff_b >>= 1
            else:
                u_coeff_b = (u_coeff_b + b) >> 1
                v_coeff_b = (v_coeff_b - a) >> 1

        if u >= v:
            u -= v
            u_coeff -= u_coeff_b
            v_coeff -= v_coeff_b
        else:
            v -= u
            u_coeff_b -= u_coeff
            v_coeff_b -= v_coeff
            
    if u == 0:
        return v << shift, u_coeff_b, v_coeff_b
    else:
        return u << shift, u_coeff, v_coeff
    
print(xgcd(48, 28))
print(binary_xgcd(48, 28))



#!/usr/bin/env python
# coding: utf-8

# 1. Írj programfüggvényt, amely az Euler\-féle φ függvény értékét számolja ki! Ellenőrzéshez használható az **euler\_phi** parancs.  
# 
# 
# 

# In[5]:


def ephi(n):
    c = 0
    for i in range(n):
        if gcd(i, n) == 1:
            c += 1
    return c

print(euler_phi(49))
print(ephi(49))


# 2. Írj programot, amely egy n∈N esetén megkeresi azt az m legkisebb természetes számot, amelyre φ\(m\)=n, illetve jelzi ha nincs ilyen!  
# 
# 

# In[2]:


def minphi(n):
    m = 1
    i = euler_phi(m)
    while i != n:
        if m > n + 1:
            return "Nincs"
        m += 1
        i = euler_phi(m)
    return m
    
minphi(100)


# ### Valószínűségi prímtesztek
# 
# 3. Írj programot, amely a bemenetként adott számhalmazban megkeresi a Carmichael számokat \(lásd jegyzetben: Elemi számelmélet/Euler \-Fermat \-tétel\).  
# 
# 

# In[4]:


def find_carmichael(A):
    L = []
    for a in A:
        if is_prime(a):
            continue
        
        skip = False
        for b in range(2, a):
            if gcd(a, b) == 1 and pow(b, a-1, a) != 1:
                skip = True
                break
                
        if skip:
            continue
            
        L.append(a)
    return L
        

cns = find_carmichael(set(range(2,1000)))
assert 561 in cns


# 4. Írj programot, amely egy **m** szám esetén meghatározza azt a legkisebb 1&lt;**a** természetes számot, amelyre **a^\(m−1\)** nem 1 modulo
#    m!  
# 
# 

# In[5]:


def first_base(m):
    for a in range(2, m):
        if pow(a, m-1, m) != 1:
            return a
    return "Nincsen"
    
assert 2 == first_base(18)
assert 3 == first_base(645)


# 5. Keresd meg azt a legkisebb összetett számot, amely esetén a Fermat\-tétel feltétele igaz a=2,3,4,5\-re és nem Carmichael szám!  
# 
# 

# In[29]:


for n in range(2, 10000):
    if not is_prime(n):
        if (power_mod(2, n-1, n) == 1 and
            power_mod(3, n-1, n) == 1 and
            power_mod(4, n-1, n) == 1 and
            power_mod(5, n-1, n) == 1):
            if n not in find_carmichael([n]):
                print(n)
                break


# 6.\* Valósíts meg a Fermat prímtesztet és hasonlítsd össze a futási idejét a próbaosztásos prímtesztével 10^8 nagyságrendű számok esetén. Hasonlítsd össze a futási időt a primszita esetén is de kisebb számokra \(4\-5jegyű, a gép kapacitásától függő méretre\).   
# 
# 

# In[4]:


def fermat_prim(p):
    a = randint(2, p-2)
    return power_mod(a, p-1, p) == 1

def proba_prim(n):
    i = 2
    while i * i < n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 1
    return True

def eratos(l, i):
    if i >= len(l):
        return l
    k = l[i]
    return eratos([n for n in l if n == k or n % k != 0], i+1)


import time
N = 10^8 + 5
start_time = time.time()
fermat_prim(N)
fermat_time = time.time() - start_time

start_time = time.time()
proba_prim(N)
proba_time = time.time() - start_time

N = 10^3
numbers = list(range(2, nth_prime(N)+1))
start_time = time.time()
eratos(numbers, 0)
erattos_time = time.time() - start_time

(fermat_time, proba_time, erattos_time)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ### Diofantikus egyenletek
# 
# 1. Valósítsd meg a LinDiofantianEq osztályt a következőknek megfelelően!
#    - Konstruktorában megadható az a,b,c értékek.
#    - Van egy **is\_solvable** függvénye.
#    - Fel tudja sorolni a megoldásokat egy **next\_solution** és egy **prev\_solution** függvény segítségével.
#    - Az első megoldás, amivel a **next\_solution** visszatér az legyen, amely esetén az x a legkisebb nemnegatív szám.
#    - Csak egy megoldást tároljunk az objektum használata közben.  
# 
# 

# In[3]:


class LinDiofantianEq:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.gcd, self.x0, self.y0 = self.gcd_extended(abs(a), abs(b))
        
        self.x0 *= c // self.gcd
        self.y0 *= c // self.gcd
        
        self.step_x = self.b // self.gcd
        self.step_y = -self.a // self.gcd
        
        self.current_x = self.x0
        self.current_y = self.y0
        
    def gcd_extended(self, a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.gcd_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    def is_solvable(self):
        return self.c % self.gcd == 0
    
    def next_solution(self):
        self.current_x += self.step_x
        self.current_y += self.step_y
        return (self.current_x, self.current_y)
    
    def prev_solution(self):
        self.current_x -= self.step_x
        self.current_y -= self.step_y
        return (self.current_x, self.current_y)
    
E = LinDiofantianEq(10,22,100)
E.next_solution()


# 2. Hányféleképpen tudunk kifizetni 100000 pengőt 47 és 79 pengős érmékkel?  
# 
# 

# In[4]:


# a  brute force nem megengedett, használd  az előző feladat megoldását
E = LinDiofantianEq(47, 79, 100000)
count = 0
k_min = (-E.current_x + E.step_x - 1) // E.step_x
k_max = E.current_y // -E.step_y
count = max(0, k_max - k_min + 1)

print(count)


# ### Kongruencia
# 
# 

# 1. Írj programot, amely egy egész számokat tartalmazó halmaz elemeit osztályozza modulo m, ahol az m a második paraméter.  
# 
# 

# In[7]:


s = set(range(5, 25 + 1))
m = 5
modulos = {}
for n in s:
    if n % m in modulos:
        modulos[n % m].append(n)
    else:
        modulos[n % m] = [n]
        
modulos


# 2. Írj eljárást lineáris kongruenciák megoldására! Ellenőrzéshez használható a **solve\_mod** parancs.  
# 
# 

# In[5]:


def lin_kong(a, b, m):
    lko, x, y = xgcd(a, m)
    if b % lko != 0:
        return
    x0 = (x * (b // lko)) % m
    return [(x0 + i * (m // lko)) % m for i in range(lko)]

a, b, m = 14, 30, 100
print(solve_mod(a*x == b, m))
print(lin_kong(a, b, m))


# 3. Írj programot, amely kiszámolja első paraméterének moduláris inverzét modulo a második paraméter! Ellenőrzéshez használható az **inverse\_mod** parancs.  
# 
# 

# In[8]:


def modin(a,m):
    gcd, x, y = xgcd(a, m)
    if gcd != 1:
        raise Exception("Nincs inverze")
    return x % m

print(modin(3, 11))
print(inverse_mod(3, 11))


# 4. Írj eljárást, amely a kínai maradéktétel megoldását állítja elő. Az programnak két lista típusú bemenete legyen, az egyik a kínai maradéktételnél szereplő c számok a másik pedig a \(páronként relatív prím\) modulusok. Ellenőrzéshez használható a például a **crt** parancs.  
# 
# 

# In[6]:


cs = [2, 3, 2]
ps = [3, 5, 7]

def kin_mar(cs, ps):
    N = 1
    for p in ps:
        N *= p
        
    x = 0
    for i in range(len(cs)):
        Ni = N // ps[i]
        inv = pow(Ni, -1, ps[i])
        x += cs[i] * Ni * inv
    
    return x % N

print(crt(cs, ps))
print(kin_mar(cs, ps))


# 5. Írj eljárást amely lineáris kongruencia\-rendszereket old meg! A programnak három lista típusú bemenete van:
#    - bal oldalak együtthatói \(ai\),
#    - jobb oldalak együtthatói \(bi\),
#    - modulusok \(mi\).  
# 
# 

# In[7]:


ai = [2, 3, 2]
bi = [3, 1, 2]
mi = [3, 5, 7]

def kong_rendsz(ai, bi, mi):
    cs = []
    for a, b, m in zip(ai, bi, mi):
        sol = lin_kong(a, b, m)
        cs.append(sol[0])
        
    solution = kin_mar(cs, mi)
    
    N = 1
    for m in mi:
        N *= m
        
    return solution, N

print(kong_rendsz(ai, bi, mi))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# **Prímek**
# 
# 1. Keressük meg az első p prímet amelyre fennáll a következő:
# 	p>100, p+6, p+12 és p+18 is prím.
# 
# 2. Hozz létre egy listát az első 100 prímszámból, és számítsd ki az összegüket.
# 
# 3.  Legyen n=100. Halmazokat használva számold meg hány olyan egész szám van a [0,n] intervallumban, melyek nem oszthatók sem 2-vel, sem 3-mal, sem 5-tel.  Ismételd ezt meg n=1000-re és n=10000-re is.
# 

# In[26]:


#Segítség: is_prime, next_prime, nth_prime, prime_pi
# 1. megoldas 251
p = 0
while (p <= 100) or (not is_prime(p+6)) or (not is_prime(p+12)) or (not is_prime(p+18)):
    p = next_prime(p)
p


# In[12]:


sum = 0
for i in range(1, 101):
    sum += nth_prime(i)
sum


# In[21]:


def f(n):
    a = set([ i for i in range(n) if not (i % 2)])
    b = set([ i for i in range(n) if not (i % 3)])
    c = set([ i for i in range(n) if not (i % 5)])
    return len(a.intersection(b, c))

print(f(100))
print(f(1000))
print(f(10000))


# **Gráfok**
# 
# 1. Írjunk egy függvényt, amely segítségével kirajzoljuk azt a gráfot, aminek a csúcsai 1 és N közötti egész számok, és élek azon csúcsok között vannak, amelyeknek összege prímszám!
# 2. Készíts egy függvényt ami egy n természetes számot kap paraméterül és készít egy olyan gráfot aminek N csúcsa van,  és kető csúcs között akkor van él ha egyik osztója a másiknak.
# 3. Készíts egy függvény ami egy gráfot kap paraméterül és visszaadja a gráf komplementerét.
# 4. Készíts egy függvényt ami egy adott gráfot bejárja mélységivel/szélleségivel.
# 
# 

# In[38]:


def f(N):
    g = Graph([Set([1..N]), lambda i,j: is_prime(i+j)])
    g.show()
    
f(10)


# In[44]:


def f2(n, N):
    g = Graph([Set([1..N]), lambda i, j: i%n or n%i])
    g.show()
    
f2(2, 10)


# In[ ]:


def komp(g):
    # Készíts egy függvény ami egy gráfot kap paraméterül és visszaadja a gráf komplementerét.
    n = g.order()
    K = graphs.CompleteGraph(n)
    return K.difference(g)

    


# **Számrendszerek**
# 
# Készíts egy 'list_to_number' függvényt ami egy listát és egy 'd' alapot kap paraméterül és a lista elemeit mint a 'd' alapu számrendszerbeli felítását a számnak kezeli és visszaalakítja 10-es számrendszerbe a számot. pld: ([1, 0, 0], 2)  bemenetre 2^3 = 8-t ad vissza.
# 
# Készítsd el ennek a fordítottját is, tehát paraméterül egy számot és egy alapot kap amit vissszaalakít listává. 
# Az egyes helyiérték helyét szabadon megválaszthatod a tömbe de mindkét feladatnál egyformán használd. 

# In[6]:


def list_to_number(l, d):
    number = 0
    for i, digit in enumerate(reversed(l)):
        number += digit * (d ** (i+1))
    return number

list_to_number([1, 0, 0], 2)

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = 21
b = 10
print("Division (result is rational)       a/b  = ", a/b)
print("Floor division (result is integer): a//b = ", a//b)
print("Remainder:                          a%b  = ", a%b)

print("Quotient and remainder:             a.quo_rem(b)          -> ", a.quo_rem(b))
print("Whether one number divides another: a.divides(b)          -> ", a.divides(b))
print("Divisors:                           a.divisors()          -> ", a.divisors())
print("Number of divisors:                 number_of_divisors(a) -> ", number_of_divisors(a))
print("                                    sigma(a,0)            -> ", sigma(a,0))
print("Sum of divisors:                    sigma(a,1)            -> ", sigma(a,1))
print("Factorization:                      a.factor()            -> ", a.factor())


# 1. **Feladat:**
#    Írd meg azt a függvényt, amely eldönti, hogy az első argumentuma osztható\-e a másodikkal az alábbi példán kívűl még 4 különböző módon!
# 
# 

# In[ ]:


# példa:
def divides0(a,b):
     return (a/b).is_integer()
    
print("2|5: ", divides0(5,2))
print("3|6: ", divides0(6,3))


# In[ ]:


def divides1(a, b):
    return b.divides(a)

def divides2(a, b):
    return a % b == 0

def divides3(a, b):
    return a // b * b == a

def divides4(a, b):
    return a.quo_rem(b)[1] == 0 

print("2|5: ", divides1(5,2))
print("3|6: ", divides1(6,3))

print("2|5: ", divides2(5,2))
print("3|6: ", divides2(6,3))

print("2|5: ", divides3(5,2))
print("3|6: ", divides3(6,3))

print("2|5: ", divides4(5,2))
print("3|6: ", divides4(6,3))


# 2.**Feladat:**  
# 
# Írj programot, amely egy adott számhalmaz esetén megszámolja hány él van az oszthatóság relációhoz tartozó Hasse\-diagramban! Ellenőrzésre használható az alábbi kódrészlet.
# 

# In[ ]:


k = 180
P = Poset((Set([2..k]), lambda a,b: b % a == 0)) #parameters set, relation as a lambda function
len(P.cover_relations_graph().edges())


# In[ ]:


k = 180
P = Poset((Set([2..k]), lambda a,b: b % a == 0))
vs = list(reversed(P.cover_relations_graph().vertices()))
es = 0

for i, e in enumerate(vs):
    temp = []
    for j in vs[i+1:]:
        if e % j == 0:
            temp.append(j)
    k = len(temp)
    for j, t in enumerate(temp):
        for x in temp[j+1:]:
            if t % x == 0:
                k -= 1
                break
    es += k
es


# 3. **Feladat:**
#    Írj programot, amely egy adott egész szám esetén kiírja osztóinak számát, illetve osztóinak összegét! Ellenőrzéshez használhatjuk a sigma\(n,0\) és sigma\(n,1\) parancsokat.  
# 
# 

# In[ ]:


def num_of_divisors(a):
    c = 0
    for i in range(1, a+1):
        if a % i == 0:
            c+=1
    return c
    
def sum_of_divisors(a):
    s = 0
    for i in range(1, a+1):
        if a % i == 0:
            s+=i
    return s

#test
try: 
    for tc in range(2,100):
        assert num_of_divisors(tc) == sigma(tc,0)
        assert sum_of_divisors(tc) == sigma(tc,1)
except AssertionError:
    print("Test failed for ", tc)
else:
    print("Ok")


# In[ ]:





# 4. **Feladat:**
#    Írj programot, amely a természetes számok egy adott halmazában megkeresi a tökéletes számokat!  
# 
# 

# In[ ]:


S = {2,3,4,6,124}
def perfect_numbers(s):
    perfect = []
    for n in s:
        if sum_of_divisors(n) - n == n:
            perfect.append(n)
    return set(perfect)
#run
print("Perfect numbers of ", S, ": ", perfect_numbers(S))


# In[ ]:





# 5. **Feladat \(Hányados\-sorozat\)**
# 
# Természetes számok esetén definiálhatjuk a következő sorozatot:s\_0 = n, s\_{i\+1} = sigma\(s\_i\) \- s\_i, ahol sigma\(n\) az n osztóinak összege.
# A sorozat vagy terminál nulla értékkel, vagy periodikussá válik. Készíts programot, amely egy adott természetes szám esetén kiszámolja az fenti sorozatot! Amennyiben a sorozat nem terminál, akkor az első periódus legyen az eredmény!  
# 
# 

# In[ ]:


def s(n):
    s_i = n
    sorozat = []
    
    while s_i != 0:
        if s_i in sorozat:
            #return sorozat # csak a periodust kell visszaadni 
            return sorozat[sorozat.index(s_i):] #a periodus, mivel csak ez ismétlődik
        sorozat.append(s_i)
        s_ip1 = sigma(s_i) - s_i # ezt a 2 sort össze lehet vonni, az  s_ip1 bevezetése fölösleges
        s_i = s_ip1
    return sorozat
    
s(220)


# In[ ]:




#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Prímekkel kapcsolatos fogalmak ellenörzése:
print("Is -1 a unit ", ZZ(-1).is_unit())
print("Is 2 unit in integer ring? ", ZZ(2).is_unit())
print("Is 2 unit in rational field? ", QQ(2).is_unit())
print("Is 6 irreducible? ", ZZ(6).is_irreducible())
print("Is -7 irreducible? ", ZZ(-7).is_irreducible())
print("Is 4 a prime? ", is_prime(4))
print("Is 7 a prime? ", ZZ(7).is_prime())
print("Is 7 a prime? ", 7 in Primes())



# In[ ]:


# Néhány prímekkel kapcsolatos SageMath eljárás:
print("First prime following 1000: ", next_prime(1000))
print("Largest prime below 1000: ", previous_prime(1000))
print("First 20 prime: ", primes_first_n(20))
print("Primes between 10 and 20: ", [p for p in primes(10,20)])
print("135th prime: ", nth_prime(135))



# ### **Prímek**
# 
# Feladatok: 1. Adj programot, amely megadja az összes prímet egy adott számig, azaz ugyanazt az eredmény adja mint a **primes\_first\_n\(n\)**! Használd Eratoszthenész szitájának módszerét.  
# 
# 

# In[ ]:


primes_first_n(10)
nth_prime(10)


# In[ ]:


N = 10
numbers = list(range(2, nth_prime(N)+1))

def eratos(l, i):
    if i >= len(l):
        return l
    k = l[i]
    return eratos([n for n in l if n == k or n % k != 0], i+1) # ez nem a szita algoritmusa
    
    
eratos(numbers, 0)


# 2. Írd meg az előző feladatot hatékonyabban úgy, hogy a páros számok ne is kerüljenek be a táblába!  
# 
# 

# In[ ]:


N = 10
numbers = [n for n in range(2, nth_prime(N)+1) if n == 2 or n % 2 != 0]

def eratos(l, i):
    if i >= len(l):
        return l
    k = l[i]
    return eratos([n for n in l if n == k or n % k != 0], i+1)
    
    
eratos(numbers, 0)


# 3. Írd meg a prímszitát úgy, hogy a 2,3  és 5\-tel osztható számok ne kerüljenek a táblába! Ehhez a számokat 30i\+M\[j\] alakban   
#    tárold \(30=2⋅3⋅5\), ahol i∈\[1,⌈n/30⌉\]; j∈\[1,8\] és  M=\[1,7,11,13,17,19,23,29\].
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:


# a factor parancs megadja a kanonikus alakot
a = -829406174141952
F = factor(a)
print("Canonical form of", a, ":             ", F)
print("Unit parti of", a, ":                 ", F.unit())
print("Prime divisors of", a, ":             ", [t[0] for t in F])
print("Prime divisors with powers for", a, ":", [t for t in F])
print("The result of the factor command is a factorization object:", type(F))


# ### Legnagyobb közös osztó
# 
# 1. Írj programot, amely adott egész számokra kiszámolja a legnagyobb közös osztót a **factor** parancs segítségével!
#    Tesztelésre használható a **gcd** _SageMath_ parancs.  
# 
# 

# In[ ]:


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


# 2. Írj programot, amely adott egész számokra kiszámolja a legkisebb közös többszöröst a **factor** parancs segítségével!
# 
# Tesztelésre használható a **lcm** _SageMath_ parancs.  
# 
# 

# In[ ]:


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


# 3. Készítsd el az euklideszi algoritmust (lásd https://compalg.elte.gitlab-pages.hu/dimoa-web/gyakorlatok/number_theory/lnko)  és hasonlítsd össze a korábbi legnagyobb közös osztót számoló program futási idejével!

# In[ ]:


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


# 4. Feladat \(Binary GCD\)
#    Írj olyan programot két természetes szám a legnagyobb közös osztójának kiszámolására, ami csak additív \(\+,\-\) és shift \(&lt;&lt;,&gt;&gt;\) műveleteket használ \(hatékony számítógépen\)! A megoldáshoz használd az alábbi összefüggéseket!
#    1. \(2a,2b\)=2\(a,b\);
#    2. \(2,b\)=1⇒\(2a,b\)=\(a,b\);  
#    3. \(a,b\)=\(a−b,b\) \(ha a és b is páratlan, akkor a−b páros lesz\).
# 
# 

# In[ ]:


def binary_gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    
    shift = 0
    while (a | b) & 1 == 0: # ez az eset is megérdemli, hogy bekerüljön a nagy while-ba, mert még előfordulhat h a paraméterek teljesítik ezt a feltételt
        a >>= 1
        b >>= 1
        shift += 1
       
    while a & 1 == 0: # ez is
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


# In[ ]:





# 5. Írj programot, ami a bővített Euklideszi\-algoritmust valósítja meg természetes számokra! Ellenőrzéshez használható az **xgcd** parancs.  
# 
# 

# In[ ]:





# 6. Implementáld a bináris gcd bővített változatát!

# In[ ]:





# In[ ]:




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

# In[ ]:


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
        
        self.current_x = self.x0 # ehelyett át kell állítania  legnagyobb negatív x-re és y-t a neki megfelelő értékre
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

# In[ ]:


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

# In[ ]:


s = set(range(5, 25 + 1))
m = 3
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

# In[ ]:


def lin_kong(a, b, m):
    lko, x, y = xgcd(a, m) # lnko a magyar röviditése
    if b % lko != 0:
        return "Nem megldható!"
    x0 = (x * (b // lko)) % m
    return [(x0 + i * (m // lko)) % m for i in range(lko)]

a, b, m = 14, 30, 100
print(solve_mod(a*x == b, m))
print(lin_kong(a, b, m))
# szép munka, tetszik, hogy a tesztet is beírtad


# 3. Írj programot, amely kiszámolja első paraméterének moduláris inverzét modulo a második paraméter! Ellenőrzéshez használható az **inverse\_mod** parancs.  
# 
# 

# In[ ]:


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

# In[ ]:


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

# In[ ]:


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




def ephi(n):
    c = 0
    for i in range(1,n): # 0rra nem érdemes nézni
        if gcd(i, n) == 1:
            c += 1
    return c

print(euler_phi(49))
print(ephi(49))

def minphi(n):
    m = 1
    i = euler_phi(m)
    while i != n:
        if prime_pi(m) > n: # adtam egy pontosabb becslést
            return "Nincs"
        m += 1
        i = euler_phi(m)
    return m
    
minphi(100)

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

def first_base(m):
    for a in range(2, m):
        if pow(a, m-1, m) != 1:
            return a
    return "Nincsen"
    
assert 2 == first_base(18)
assert 3 == first_base(645)

""" for n in range(2, 10000):
    if not is_prime(n):
        if (gcd(n, 2) == 1 and power_mod(2, n-1, n) == 1 and
            gcd(n, 3) == 1 and power_mod(3, n-1, n) == 1 and
            and power_mod(4, n-1, n) == 1 and
            gcd(n, 5) == 1 and power_mod(5, n-1, n) == 1):
            if n not in find_carmichael([n]):
                print(n)
                break """

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


def gyors_hat(a, k):
    bink = k.str(base=2)
    n = len(bink) - 1
    r = a
    while n > 0:
        r = r*r
        if bink[n] == '1':
            r = r*a
        n = n - 1
    return r

import time
start = time.time()
gyors_hat(2, 100)
end = time.time()
print(end-start)

def hatvanyok(a, m):
    h = set()
    hatv = a % m
    while hatv not in h:
        h.add(hatv)
        hatv = (hatv * a) % m
    return h

hatvanyok(3, 7)

def gener(p):
    gs = []
    for g in range(1, p):
        if len(set([pow(g, k, p) for k in range(1, p)])) == p - 1:
            gs.append(g)
    return gs

gener(7)

def bruteF(a, m, p):
    for e in range(p):
        if pow(a, e, p) == m:
            return x
    return None

a = 5
m = 5
p = 23

from time import *

start_time = time()
bruteF(a, m, p)
brute_time = time() - start_time

start_time = time()
discrete_log(m, a, p)
sage_time = time() - start_time
print(brute_time, sage_time)

import random

class DH_participant:
    def __init__(self, p, g):
        self.p = p
        self.g = g
        self.private = random.randint(2, p-2)
        self.public = pow(g, self.private, p)
    
    def get_pub(self): # returns with the public parameter
        return self.public
    
    def calculate_common_key(self, pub_of_other):
        return pow(pub_of_other, self.private, self.p)
    
Alice = DH_participant(65537, 2)
Bob   = DH_participant(65537, 2)
assert Alice.calculate_common_key(Bob.get_pub()) == Bob.calculate_common_key(Alice.get_pub())

class RSA(object):
    def __init__(self, length):
        # uniformly chosen prime is not a good idea in real life 
        p = random_prime(2^(length-2), lbound=2^(length-3))
        q = random_prime(2^(length+2), lbound=2^(length+1))
        
        self.__n = p * q
        self.__phin = (p-1) * (q-1)
        self.__e = 3
        
        while gcd(self.__e, self.__phin) != 1:
            self.__e += 2
        
        self.__d = inverse_mod(self.__e, self.__phin)
    
    def public_key(self):
        return (self.__n, self.__e)
    
    @staticmethod
    def encrypt(pubkey, message):
        n, e = pubkey
        return power_mod(message, e, n)
    
    def decrypt(self, secret):
        return power_mod(secret, self.__d, self.__n)
    
    def sign(self, message):
        return power_mod(message, self.__d, self.__n)
    
    @staticmethod
    def verify(pubkey, signed_message):
        n, e = pubkey
        return power_mod(signed_message, e, n)


#!/usr/bin/env python
# coding: utf-8

# Ora4/5. Írj eljárást amely lineáris kongruencia\-rendszereket old meg! A programnak három lista típusú bemenete van:
# 
# - bal oldalak együtthatói \(ai\),
# - jobb oldalak együtthatói \(bi\),
# - modulusok \(mi\).  
# 
# 

# In[ ]:


# ax == b (mod m) és ha a* mod inverze a-nak: x==(a a*)x == a*b mod m
# x == c (m)
# kmt használata c és m listára
def kongruenia_mo(A, B, M):
    C = []
    newM = []
    for a, b, m in zip(A, B, M):
        lnko = gcd(a, m)
        if lnko == 1:
            ainv = inverse_mod(a,m)
            C.append(ainv*b % m)
            newM.append(m)
        elif not b % lnko == 0:
#             raise ValueError("A kongruencia rendszer nem megoldhato!")
            return "A kongruencia rendszer nem megoldhato!"
        else:
            am = a // lnko
            bm = b // lnko
            mm = m // lnko
            ainv = inverse_mod(am,mm)
            C.append(ainv*bm % mm)
            newM.append(mm)
    # kinai maradek tetel C, newM listára
    return crt1(C, newM)

La = [1,2,3]
Lb = [2,3,4]
Lm = [3,5,7]
x = kongruenia_mo(La, Lb, Lm) # a modulok szorzataban megoldás x == 104 mod 3*5*7
print(x)

for i in range(len(La)):
    print(La[i]*x % Lm[i] == Lb[i])


# In[ ]:


def crt1(C, M):
#     m1x + m2y = 1 -> c = m1 x c2 + m2 y c1 == x mod m1 m2
    Mall = prod(M)
    xall = 0
    for ci, mi in zip(C,M):
        Mi = Mall//mi
        z = inverse_mod(Mi, mi)
        xall += Mi*z*ci
    return xall % Mall

C = [2, 3, 4]
M  = [3,4,5]
crt(C,M) == crt1(C,M)


# In[ ]:


prod([1,2,3])


# Ora6/5. Írj programot, amely egy **Diffie\-Hellman** kulcscsere folyamatát szemlélteti, G=Zp \(p prím\) választással. \(lásd [https://compalg.elte.gitlab\-pages.hu/dimoa\-web/gyakorlatok/coding\_theory/cryptography/dh](https://compalg.elte.gitlab-pages.hu/dimoa-web/gyakorlatok/coding_theory/cryptography/dh) \)  
# 
# 

# In[ ]:


class DH_participant:
    def __init__(self, p, g):
        self.p = p
        self.g = g
        self.x = randint(2,p-1)
        self.pk = g^self.x % p
        
    def get_pub(self): # returns with the public parameter
        return self.pk
    
    def calculate_common_key(self, pub_of_other):
        return pub_of_other^self.x % self.p
    
Alice = DH_participant(65537, 2)
Bob   = DH_participant(65537, 2)
Alice.calculate_common_key(Bob.get_pub()) == Bob.calculate_common_key(Alice.get_pub())


# In[ ]:


randint(2,5)


# In[ ]:





# Ora6/6. Írj osztályt, amely adott publikus paraméterek esetén megvalósítja a titkosításra és hitelesítésre is használható RSA sémát! \(https://compalg.elte.gitlab\-pages.hu/dimoa\-web/gyakorlatok/coding\_theory/cryptography/rsa \)  
# 
# 

# In[ ]:


class RSA(object):
    def __init__(self, length):
        # uniformly chosen prime is not a good idea in real life 
        p = random_prime(2^(length-2), lbound=2^(length-3))
        q = random_prime(2^(length+2), lbound=2^(length+1))
        self.__n = p*q
        self.__phin = (p-1)*(q-1) # lassu: euler_phi(n)
        self.__e = 3 #should choose this more carefully
        while gcd(self.__e, self.__phin) != 1:
            self.__e += 2
        self.__d = inverse_mod(self.__e, self.__phin)

    def public_key(self):
        return self.__n, self.__e
    
    @staticmethod
    def encrypt(pubkey, message):
        return message^pubkey[1] % pubkey[0]
    
    def decrypt(self, secret):
        return secret^self.__d % self.__n
    
    def sign(self, message):
        m = h(message)
        s = m^self.__d % self.__n
        return (message,s)
    
    @staticmethod
    def verify(pubkey, signed_message):
        return h(signed_message[0]) == signed_message[1]^pubkey[1] % pubkey[0]
    def h(message):
        return message


# In[ ]:




# Polinomok definiálása
# 1. Ezzel a módszerrel nem kapunk polinomot, pár függvény ígyis müködhet de inkább ne használd ezt.
f = 4*x^2+3*x+2
print("Legyen f = ", f)
print("1. esetben f típusa:", type(f))

# 2. 
R = ZZ['x'] # Egészek feletti polinomok
p1 = 4*x^2+3*x+2
p2 = R(4*x^2+3*x+2)
print(f"2. esetben az f típusa: {type(p1)}")
print(f"2. esetben az R(f) típusa: {type(p2)}")

# 3.
R  = PolynomialRing(QQ, 'x')
print("R és QQ['x'] megegyeznek:", type(R) == type(QQ['x']))
f = R(4*x^2+3*x+2) # polinom
f1 = 4*x^2+3*x+2 # még mindig nem polinom
# print(f)
print("3. esetben f típusa:",type(f))
print("3. esetben f1 típusa:",type(f1))

print("Vigyázz, mert Expression típutú értéket össze tudsz szorozni polinommal de az eredmény:", type(x*f))
print("Előző szorzat polinom típusú ha 'R(x)*f' alakot használsz.")

# 4. 
""" RZ.<x> = PolynomialRing(ZZ) # Z[x] feletti polinomok
f = 4*x^2+3*x+2 #polinom """
# print(f)
print("4. esetben f típusa:",type(f))

# 5. Z_m feletti polinomok
# y-t már kell definiálni ha használni akarjuk
var('y')
""" RZ3.<y> = PolynomialRing(IntegerModRing(3)) # Z_3 struktura 
f = 4*y^3+3*y+2 """
print("5. esetben legyen f =", f)
print("5. esetben f típusa:", type(f))

# 6.  Listából is konstruálható, vigyázzunk az együtthatók sorrendjére!
f = ZZ['x']([1,2,0,3, 0, 5])
print("6. esetben legyen f =", f)
print("6. esetben f típusa:", type(f))


#7. többváltozós polinomok
var('z,y1')
f=ZZ['x,z,y1'](y1^2+5*y1-102 + x + z)
print("7. esetben legyen f =", f)
print("7. esetben f típusa:", type(f))

# Műveletek polinomokkal
p3 = ZZ['x'](54*x^4 + 36*x^3 - 102*x^2 - 72*x - 12)
print("Legyen p = ", p3)
print("p főegyütthatója: ", p3.leading_coefficient())
print("p konstans tagja: ", p3.constant_coefficient(), p3(0))
print("", p3.coefficients()) 
print("p fokszáma: ", p3.degree())
print("p együtthatóinak listája: ", p3.list())
print("p kiértékelése a 2-ben: ", p3(2))
print(f"p {x^2} melletti együthatója: ", p3[2])
print("3*p = ", 3 * p3)
print("p^5 = ", p3^5)

print("p gyökei: ", p3.roots())
print("p gyökei komplex számok felett: ", p3.roots(ring=CC))
print("p-t polinomok szorzatára bontása: ", p3.factor())


# Maradékos osztás (ha elvégezhető)
T = ZZ['x']
f = T(42*x^4 - 7*x^3 + 13*x^2 + 43*x - 12)
g = T(3*x^2 - x + 1) 

print("Legyen f = ", f)
print("Legyen g = ", g)
print(f"Az f-t elosztva g-vel a hányados {f // g} és a maradék {f % g}.")


p = ZZ['x']((3*x^8+5*x^6-11*x^3+7*x^2-15*x+8)*(x+1))*(x+10)
q = ZZ['x']((x^3+1)*(x+2))
print("Legyen p = ", p)
print("Legyen q = ", q)
print("p és q polinomok legnagyobb közös oszó polinomja: ", gcd(p,q)) # lehet p.gcd(q) alakba is írni



# Segítség: a roots függvény párokad ad vissza ahol az első érték az az c amire p(c) = 0, a második pedig, hogy hányszoros gyök vagyis a szorzat alakban az (x-c) hányadik hatványon jelenik meg
print("p gyökei: ", p.roots())


def n_polly(poly):
    R = poly.parent()
    roots = poly.roots()
    null_polynomial = R(1)
    for root, multiplicity in roots:
        null_polynomial *= (R.gen() - root)^multiplicity
    return null_polynomial

class my_poly(object):
    def __init__(self, F):
        self.coefficients = F
        
    def deg(self):
        return len(self.coefficients) - 1 if self.coefficients else -1
    
    def __add__(self, other):
        max_deg = max(self.deg(), other.deg())
        result = [0] * (max_deg + 1)
        
        for i in range(self.deg() + 1):
            result[i] += self.coefficients[i]
        for i in range(other.deg() + 1):
            result[i] += other.coefficients[i]
            
        return my_poly(result)
        
    def __mul__(self, other):
        result_deg = self.deg() + other.deg()
        result = [0] * (result_deg + 1)
        
        for i in range(self.deg() + 1):
            for j in range(other.deg() + 1):
                result[i + j] += self.coefficients[i] * other.coefficients[j]
        
        return my_poly(result)
        
    def __repr__(self):
        return " + ".join(f"{coef}*x^{i}" for i, coef in enumerate(self.coefficients) if coef != 0)
    
    def eval(self, x):
        result = 0
        for coef in reversed(self.coefficients):
            result = result * x + coef
        return result


def lagrange_interp(points):
    R = PolynomialRing(QQ, 'x')
    x = R.gen()
    
    n = len(points)
    P = R(0)
    
    for i in range(n):
        xi, yi = points[i]
        Li = R(yi)
        
        for j in range(n):
            if i != j:
                xj = points[j][0]
                Li *= (x - xj)
                Li //= (xi - xj)
        P += Li
        
    return P

L = [(1, 2), (3, 4), (5, 6)]
P = lagrange_interp(L)
Q = PolynomialRing(QQ, 'x').lagrange_polynomial(L)

print(P)
print(Q)


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
#!/usr/bin/env python
# coding: utf-8

# 1. Valósítsd meg a paritásbites kódolást páratlanra való kiegészítéssel!
# 
# 

# In[ ]:


class ParCheckCode:
    def encode(self, data):
        ones_count = data.count('1')
        if ones_count % 2 == 0:
            data += "1"
        else:
            data += "0"
        return data
        
    def decode(self, cdata): # hibás szó estén jelezzük
        ones_count = cdata.count('1')
        
        if ones_count % 2 == 0:
            raise ValueError("paritas nem paratlan")
        return cdata[:-1]

p = ParCheckCode()
print(p.encode("1010"))
print(p.decode(p.encode("1010")))


# 2. Valósítsd meg a kétdimenziós paritásbites kódolást!
# 
# 

# In[ ]:


class TwoDimParCheckCode:
    self.p = ParCheckCode()
    
    def encode(self, data): # a legkisebb valódi osztó alapján darabold fel
        lvo = None
        for i in range(2, len(data) + 1):
            if len(data) % i == 0:
                lvo = i
        if lvo is None:
            lvo = len(data)
        rows = lvo
        cols = len(data) // lvo
        
        matrix = [list(data[i * cols:(i + 1) * cols]) for i in range(rows)]
        for i in range(rows):
            parity_bit = str(matrix[i].count('1') % 2)
            matrix[i].append(parity_bit)
                    
        last_row = []
        for j in range(cols + 1):
            col_bits = [matrix[i][j] for i in range(rows)]
            parity_bit = str(col_bits.count('1') % 2)
            last_row.append(parity_bit)
        matrix.append(last_row)
        return matrix
        
        
    def decode(self, cdata): # corrects 1 error, notifies if there is 2
        rows = len(cdata) - 1
        cols = len(cdata[0]) - 1
        error_row = None
        error_col = None
                
        for i in range(rows):
            parity_bit = str(cdata[i][:cols].count('1') % 2)
            if parity_bit != cdata[i][cols]:
                error_row = i
                    
        for j in range(cols):
            col_bits = [cdata[i][j] for i in range(rows)]
            parity_bit = str(col_bits.count('1') % 2)
            if parity_bit != cdata[rows][j]:
                error_col = j
                    
        if error_row is not None and error_col is not None:
            cdata[error_row][error_col] = '1' if cdata[error_row][error_col] == '0' else '0'
        elif error_row is not None or error_col is not None:
            raise ValueError("több hiba")
                
        original_data = ''
        for i in range(rows):
            original_data += ''.join(cdata[i][:cols])
        return original_data
        
        
tp = TwoDimParCheckCode()
print(tp.encode("010101"))


# 3. Írj programot, amely egy standard alakú generátormátrixhoz elkészíti annak hibaellenőrző\-mátrix párját!  
# 
# 

# In[ ]:


def hibaellenorzo_matrix(G):
    k, n = G.nrows(), G.ncols()
    P = G[:, k:]     
    
    I_r = identity_matrix(n - k)
    H = block_matrix([[P.transpose()], [I_r]])
    
    return H


G = Matrix([[1, 0, 0, 1, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1]])

H = hibaellenorzo_matrix(G)
print(G)
print(H)


# 4. Írj programot, amely egy standard alakú hibaellenőrző\-mátrixhoz elkészíti annak generátormátrix párját!  
# 
# 

# In[ ]:


def generator_matrix(H):
    n = H.ncols()
    k = n - H.nrows()  
    G = Matrix(GF(2), k, n)
    
    G[:, :k] = identity_matrix(GF(2), k)
    
    for i in range(k, n):
        G[:, i] = H.transpose().column(i - k)
    
    return G


# 5* Adj programot, amely egy generátormátrixhoz meghatározza a vele ekvivalens szisztematikus kód generátormátrixát! (opcionális, nem plusz pontra)
# 
# 

# In[ ]:





# In[ ]:




C_words = ['00000', '00111', '11001', '11110']
C = [vector(GF(2), [int(bit) for bit in word]) for word in C_words]

G = matrix(C).transpose()
G = G.echelon_form()

n = G.ncols()
k = G.nrows()
H = G.right_kernel_matrix()

n = len(C_words[0])
error_vectors = [vector(GF(2), [1 if i == j else 0 for i in range(n)]) for j in range(n)]

syndrome_table = {}
for e in error_vectors:
    s = H * e.column()
    syndrome_table[tuple(s)] = e

for s in syndrome_table:
    print(f"Szindróma: {s}, Hibavektor: {syndrome_table[s]}")

def generator_matrix_standard_form(g_coeffs, n):
    k = len(g_coeffs)
    G = []
    for i in range(k):
        row = [0]*i + g_coeffs + [0]*(n - k - i)
        G.append(row[:n])
    G = Matrix(GF(2), G)
    G_std = G.echelon_form()
    return G_std

g = [1, 0, 1, 1]
n = 7
G_standard = generator_matrix_standard_form(g, n)
print(G_standard)

def generator_matrix(g_coeffs, n):
    k = n - len(g_coeffs) + 1 
    G = []
    
    for i in range(k):
        row = [0]*i + g_coeffs + [0]*(n - len(g_coeffs) - i)
        G.append(row)
        
    return Matrix(GF(2), G)

g = [1, 0, 1, 1]
n = 7 
G = generator_matrix(g, n)
print(G)

def gen_divisors_poly(n, p):
    R = PolynomialRing(GF(p), "x")
    x = R.gen()
    f = x^n - 1
    factors = f.factor()
    from itertools import combinations
    all_generators = []
    factor_list = [(factor, mult) for factor, mult in factors]
    for i in range(1, len(factor_list) + 1):
        for combo in combinations(factor_list, i):
            g = R(1)
            for factor, _ in combo:
                g *= factor
                
            if g.degree() < n:
                all_generators.append(g)
    return all_generators

n = 7
p = 2
generators = gen_divisors_poly(n, p)
for g in generators:
    print(f"Generátorpolinom: {g}")

def code_polynomial(m_coeffs, g_coeffs):
    R = PolynomialRing(GF(2), 'x')
    m = R(m_coeffs)
    g = R(g_coeffs)
    c = m * g
    return c

m_coeffs = [1, 0, 1]
g_coeffs = [1, 0, 1, 1]
c = code_polynomial(m_coeffs, g_coeffs)
print(f'Kódpolinom c(x): {c}')





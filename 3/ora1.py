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


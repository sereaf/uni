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





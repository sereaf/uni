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

# példa:
def divides0(a,b):
     return (a/b).is_integer()
    
print("2|5: ", divides0(5,2))
print("3|6: ", divides0(6,3))

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

k = 18
P = Poset((Set([2..k]), lambda a,b: b % a == 0)) #parameters set, relation as a lambda function
len(P.cover_relations_graph().edges())

k = 18
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



S = {2,3,4,6,124}
def perfect_numbers(s):
    perfect = []
    for n in s:
        if sum_of_divisors(n) - n == n:
            perfect.append(n)
    return set(perfect)
#run
print("Perfect numbers of ", S, ": ", perfect_numbers(S))



def s(n):
    s_i = n
    sorozat = []
    
    while s_i != 0:
        if s_i in sorozat:
            return sorozat
        sorozat.append(s_i)
        s_ip1 = sigma(s_i) - s_i
        s_i = s_ip1
    return sorozat
    
s(10)



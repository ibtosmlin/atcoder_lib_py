#####################
# 最大公約数gcd
#####################
from fractions import gcd
from math import gcd

# print(gcd(2,6))

#####################
# 最小公倍数lcm
#####################
from fractions import gcd
from math import gcd
def lcm(a,b):
    G=gcd(a,b) #最大公約数
    L=(a//G)*b #最小公倍数
    return L

# print(lcm(2,6))

#####################
# 複数の最大公約数gcd
#####################
from math import gcd
from math import reduce
from fractions import gcd
from functools import reduce
def Gcd(list):
    gcd = 1
    G = reduce(gcd, list)
    return G

# A = [2,6,8]
# print(Gcd(A))

#####################
# 複数の最小公倍数lcm
#####################
from math import gcd
from fractions import gcd
def Lcm(list):
    L = 1
for a in list:
    L = (a // gcd(a, L))*L
    return L

# A = [2,6,8]
# print(Lcm(A))
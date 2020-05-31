#####################
# 最大公約数gcd
# 最小公倍数lcm
#####################
from fractions import gcd   #for python3.4
from math import gcd        #for python3.8

def lcm(a,b):
    G = gcd(a, b) #最大公約数
    L = (a//G)*b #最小公倍数
    return L

#print(gcd(6,8)) #2
#print(lcm(6,8)) #24

#####################
# 複数の最大公約数Gcd
# 複数の最小公倍数Lcm
#####################
from fractions import gcd   #for python3.4
from math import gcd        #for python3.8

def Gcd(lt):
    l = len(lt)
    ret = [1]*l
    ret[0] = lt[0]
    for i in range(1,l):
        ret[i] = gcd(ret[i-1], lt[i])
    return ret

def Lcm(lt):
    l = len(lt)
    ret = [1]*l
    ret[0] = lt[0]
    for i in range(1,l):
        ret[i] = (ret[i-1] // gcd(ret[i-1], lt[i])) * lt[i]
    return ret

A = [2,6,7,8]
#print(Gcd(A)) [2, 2, 1, 1]
#print(Lcm(A)) [2, 6, 42, 168]
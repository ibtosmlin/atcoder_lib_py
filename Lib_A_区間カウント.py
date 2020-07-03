###################################
# A=[0, 0, 1, 1, 1, 1, 0, 1, 1, 1]
# x=1 の区間がいくつあるか ans = 2
###################################

def Cnt_Interval(A, x):
    N = len(A)
    i = 0
    ret = 0
    while i<N:
        if A[i]<x:
            i += 1
        else:
            ret += 1
            while i<N and A[i]>=x:
                i += 1
    return ret

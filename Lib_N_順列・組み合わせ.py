##############################
# 順列・組み合わせの数
##############################

# nPr
from itertools import permutations
L = list(permutations(range(3), 2))
print(L)

#nCr
from itertools import combinations
L = list(combinations(range(3), 2))
print(L)

#product
from itertools import product
L = list(product(range(3), repeat=2))
print(L)

#product2
from itertools import product
T = [[1, 2],[3, 4, 5, 6],[7, 8, 9]]
L = list(product(*T))
print(L)

#重複も許容した組み合わせ
from itertools import combinations_with_replacement
L = list(combinations_with_replacement(range(3), 2))
print(L)

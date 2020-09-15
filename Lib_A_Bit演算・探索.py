#########################
# BIT演算
#########################

# >>は*1/2 右シフト
x>>j
# <<は*2 左シフト
x<<j
#NOT
~x
#Union
x|y
#and
x&y
#xor
x^y
#mask
x&0011000

#########################
# BIT全探索
#########################
money = 300
item = (("apple", 100), ("banana", 200), ("orange", 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    total = 0
    for j in range(n):    #
        if i >> j & 1:    #
            bag.append(item[j][0])  #
            total += item[j][1]  #
    if (total <= money):
        print(total, bag)

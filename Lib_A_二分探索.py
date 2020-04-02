####################
# めぐる二分探索
####################

arr = [1,3,5,5,5,6,7]
def is_ok(i):
    return arr[i] <= 5
    #return arr[i] < 5

#初期値設定
ok = -1
ng = 7
while ng-ok > 1:
    mid = (ok+ng) // 2 # 平均(小数切り捨て)
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
print(ok,ng) # "3,5" が出力される
#print(ok,ng) # "1,2" が出力される

####################
# bisect二分探索
####################
from bisect import bisect_left, bisect_right

arr = [1,3,5,5,5,6,7]       # 昇順にソートされている必要がある
l = bisect_left(arr, 5)     # 5が入るべき境目のうち最も左側の境目を返す
r = bisect_right(arr, 5)    # 5が入るべき境目のうち最も右側の境目を返す
print(l,r)                  # "2 5" が出力される
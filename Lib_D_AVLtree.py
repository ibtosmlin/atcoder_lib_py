#!/usr/bin python3
# -*- coding: utf-8 -*-

# AVL木

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        self.sum = data
        self.size = 1
    # データを探す
    def search(self, x):
        while self is not None:
            if self.data == x: return self
            if x < self.data:
                self = self.left
            else:
                self = self.right
        return None
    # 最小値を探す
    def search_min(self):
        while self.left is not None:
            self = self.left
        return self
    # 最下限
    def lower_bound(self, x):
        res = float("inf")
        while self is not None:
            if self.data == x: return self
            if x <= self.data:
                res = self.data
                self = self.left
            else:
                self = self.right
        return res

    # k番目を探す
    def get_kth(self, k):
        while True:
            if self is None:
                return -1
            if self.left is None:
                lsize = 0
            else:
                lsize = self.left.size
            if k == lsize:
                return self.data
            if k < lsize:
                self = self.left
            else:
                k -= lsize + 1
                self = self.right

class AVL:
# 初期化
    def __init__(self): # 初期化
        self.root = None
# 属性取得
    def get_height(self, node):
        if not node: return -1
        return node.height
    def recal_height(self, node):
        if not node: return -1
        ret = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return ret
    def get_size(self, node):
        if not node: return 0
        return node.size
    def recal_size(self, node):
        if not node: return 0
        ret = self.get_size(node.left) + self.get_size(node.right) + 1
        return ret
    def get_sum(self, node):
        if not node: return 0
        return node.sum
    def recal_sum(self, node):
        if not node: return 0
        ret = self.get_sum(node.left) + self.get_sum(node.right) + node.data
        return ret
    def get_balance(self, node):
        # 返り値>1:左の部分木が重い->右回転
        # 返り値<-1:右の部分木が重い->左回転
        if not node: return 0
        ret = self.get_height(node.left)
        ret -= self.get_height(node.right)
        return ret
# 回転
    def rotate_right(self, node):
        lc = node.left
        lrc = lc.right
        lc.right = node   # 左子lcが元のnodeの位置に上がる
        node.left = lrc   # 左子の右子lrcが元のnodeの左子に移動
        node.height = self.recal_height(node)
        lc.height = self.recal_height(lc)
        node.size = self.recal_size(node)
        lc.size = self.recal_size(lc)
        node.sum = self.recal_sum(node)
        lc.sum = self.recal_sum(lc)
        return lc
    def rotate_left(self, node):
        rc = node.right
        rlc = rc.left
        rc.left = node    # 右子rcが元のnodeの位置に上がる
        node.right = rlc  # 右子の左子rlcが元のnodeの右子に移動
        node.height = self.recal_height(node)
        rc.height = self.recal_height(rc)
        node.size = self.recal_size(node)
        rc.size = self.recal_size(rc)
        node.sum = self.recal_sum(node)
        rc.sum = self.recal_sum(rc)
        return rc
# 挿入
    def insert(self, data):
        self.root = self._insert(data, self.root)
    def _insert(self, data, node):
        if not node: return Node(data)  # 空の木ならノードを作って終わり
        if data < node.data:
            node.left = self._insert(data, node.left)
        else:
            node.right = self._insert(data, node.right)
        node.height = self.recal_height(node)
        node.size = self.recal_size(node)
        node.sum = self.recal_sum(node)
        return self.settle_unbalance(data, node)

# バランス調整
    def settle_unbalance(self, data, node):
        bal = self.get_balance(node)
        if bal > 1: # 左重
            if data < node.left.data:
            # 左子の左にデータ
                return self.rotate_right(node)  # 右回転
            if data > node.left.data:
            # 左子の右にデータ
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)  # 左回転&右回転
        if bal < -1:    # 右重
            # 右子の右にデータ
            if data > node.right.data:
                return self.rotate_left(node)  # 左回転
            if data < node.right.data:
            # 右子の左にデータ
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)   # 右回転&左回転
        return node

# 削除
    def remove(self, data):
        if self.root:
            self.root = self._remove(data, self.root)
    def _remove(self, data, node):
        if data < node.data:
            node.left = self._remove(data, node.left)
        elif data > node.data:
            node.right = self._remove(data, node.right)
        else:   # 見つかった場合
            if not node.right and not node.left:    # 削除ノードが葉の場合
                del node
            # None を返すことで、親ノードの削除子ノードへのポインタを None に変更
                return None
            # 削除ノードが左の子だけを持つ場合、ノードを削除し、左の子のノードを返す
            if not node.right:
                temp = node.left
                del node
                # 左の子のノードを返すことで、親ノードの削除子ノードへのポインタを新しい子ノードに変更
                return temp
            # 削除ノードが右の子だけを持つ場合、左の子だけの場合の逆の操作を行う
            if not node.left:
                temp = node.right
                del node
                return temp
            # 削除ノードが左右の子を持つ場合、
            # ここでは、左側のsubtreeの最大のノードを代わりのノードにすることにする。
            #  subtreeの最大のノードを取得するヘルパー関数
            def _get_max_node(node):
                if node.right:
                    return _get_max_node(node.right)
                return node
            temp = _get_max_node(node.left)
            node.data = temp.data
            # 左側のsubtreeから削除ノードと入れ替えたノードを削除
            node.left = self._remove(temp.data, node.left)

        # 単体の木の場合
        if not node:
            return node

        node.height = self.recal_height(node)
        node.size = self.recal_size(node)
        node.sum = self.recal_sum(node)
        bal = self.get_balance(node)
        if bal > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if bal < -1:
            if self.get_balance(node.left) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

# 巡回
    def traverse_inorder(self):
        if self.root:
            return self._traverse_inorder(self.root)
        else:
            return []

    def _traverse_inorder(self, node):
        ret = []
        if node.left:
            ret.extend(self._traverse_inorder(node.left))
        ret.append([node.data, node.size, node.height, node.sum])
        if node.right:
            ret.extend(self._traverse_inorder(node.right))
        return ret

# 探索
    def search(self, x):
        return self.root.search(x)

# 最小値探索
    def search_min(self):
        return self.root.search_min()

# k番目探索
    def get_kth(self, k):
        return self.root.get_kth(k)

# 最下限
    def lower_bound(self, x):
        return self.root.lower_bound(x)

# 表示
    def __str__(self):
        if self.root is None: return 'AVLtree[]'
        ret = 'AVLtree['
        for x in self._traverse_inorder(self.root):
            ret += str(x) + ', '
        ret = ret.rstrip(", ")
        ret += ']'
        return ret

##################################################


avl = AVL()
q = int(input())
for _ in range(q):
    t, a = map(int, input().split())
    if t == 1:
        avl.insert(a)
    else:
        kn = avl.get_kth(a-1)
        print(kn)
        avl.remove(kn)



#import random

#avl = AVL()
#a = [random.randint(1, 2000) for i in range(7)]
#print(a)
#for ai in a:
#    avl.insert(ai)
#print(avl.traverse_inorder())
#print('size', avl.get_size(avl.root),'height', avl.get_height(avl.root))
#print(avl.search_min().data)
#print("ti:", 3,avl.traverse_inorder()[3]) #3+1番目取得
#print("kth:", 3, avl.get_kth(3)) #3+1番目取得

#avl.remove(min(a))
#print('削除後')
#print(avl.traverse_inorder())
#print('size', avl.get_size(avl.root),'height', avl.get_height(avl.root))
#print("min:",avl.search_min().data)
#
#if avl.root.search(300) is not None:
#    print(avl.search(300))
#else:
#    print('NOdata')
#print("lb:", avl.lower_bound(300))
#print("ti:", 3,avl.traverse_inorder()[3]) #3+1番目取得
#print("kth:", 3, avl.get_kth(3)) #3+1番目取得

#print(avl.root.data)
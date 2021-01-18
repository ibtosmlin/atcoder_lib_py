#!/usr/bin python3
# -*- coding: utf-8 -*-

# minmax法
# https://atcoder.jp/contests/abc025/tasks/abc025_c

def score(board):
    ret1 = 0
    ret2 = 0
    for i in range(2):
        for j in range(3):
            ret1 += (board[i][j] == board[i+1][j]) * b[i][j]
            ret1 += (board[j][i] == board[j][i+1]) * c[j][i]
            ret2 += (board[i][j] != board[i+1][j]) * b[i][j]
            ret2 += (board[j][i] != board[j][i+1]) * c[j][i]
    return (ret1-ret2, ret1, ret2)

memo = dict()

def dfs(turn, board):
    k = str(turn)
    for i in range(3):
        for j in range(3):
            k += board[i][j]
    if k in memo:
        return memo[k]
    if turn == 9:
        memo[k] = score(board)
    elif turn%2==0: # 最小値を大きくする
        ret = -100000
        for i in range(3):
            for j in range(3):
                if board[i][j]=='z':
                    board[i][j]='o'
                    sc, ret1, ret2 = dfs(turn+1, board)
                    if ret < sc:
                        rret1 = ret1
                        rret2 = ret2
                        ret = sc
                    board[i][j]='z'
        memo[k] = (ret, rret1, rret2)
    else:            # 最大値を小さくする
        ret = 100000
        for i in range(3):
            for j in range(3):
                if board[i][j]=='z':
                    board[i][j]='x'
                    sc, ret1, ret2 = dfs(turn+1, board)
                    if ret > sc:
                        rret1 = ret1
                        rret2 = ret2
                        ret = sc
                    board[i][j]='z'
        memo[k] = (ret, rret1, rret2)
    return memo[k]

b = [list(map(int, input().split())) for i in range(2)]
c = [list(map(int, input().split())) for i in range(3)]
board = [['z']*3 for i in range(3)]

sc, ret1, ret2 = dfs(0, board)
print(ret1)
print(ret2)

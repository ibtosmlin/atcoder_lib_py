
import numpy as np

def main():
    N, W = map(int, input().split())
    wv=[None]*N
    mxw = 0
    mxv = 0
    for _ in range(N):
        v_, w_ = map(int, input().split())
        mxw = max(mxw, w_)
        mxv = max(mxv, v_)
        wv[_] = (w_, v_)

    if N<=100:
        Ga = wv[:N//2]
        Gb = wv[N//2:]
        La = [[0,0]]
        for w, v in Ga:
            tmp = La.copy()
            for wt, vt in tmp:
                if wt+w<=W:
                    La.append([wt+w,vt+v])
        La.sort(key = lambda x: x[1])
        La.sort(key = lambda x: x[0])
        Ma=[La[0]]
        wc,vc = La[0]
        for i in range(1,len(La)):
            wn,vn = La[i]
            if vn>vc:
                Ma.append([wn,vn])
                wc,vc = wn, vn

        Lb = [[0,0]]
        for w, v in Gb:
            tmp = Lb.copy()
            for wt, vt in tmp:
                if wt+w<=W:
                    Lb.append([wt+w,vt+v])
        Lb.sort(key = lambda x: x[1])
        Lb.sort(key = lambda x: x[0])
        Mb=[Lb[0]]
        wc,vc = Lb[0]
        for i in range(1,len(Lb)):
            wn,vn = Lb[i]
            if vn>vc:
                Mb.append([wn,vn])
                wc,vc = wn, vn
        ret = 0
        for wb, vb in Mb:
            ng = len(Ma)
            ok = -1
            while ng-ok>1:
                mid=(ng+ok)//2
                wa, va = Ma[mid]
                w = wa+wb
                v = va+vb
                if w<=W:
                    ok = mid
                else:
                    ng = mid
            ret = max(ret, Ma[ok][1]+vb)
        print(ret)

    elif N<=200 and mxw<=1000:
    #######################################################################
    # ナップサック
    # 重さ：Wー10**5くらい
    # 価値：N*max_Viー10**11くらい
    # dp[w]:wの重さで可能な最大の価値
    #   dp[w]とdp[w-wi]+vi(i番目のアイテムをとる場合)　との大きいほうで更新
    #######################################################################
        dp = [0] * (W+1)
        dp = np.array(dp)
        for _ in range(N):
            w_, v_ = wv[_]
            dp[w_:] = np.maximum(dp[w_:], dp[:-w_] + v_)
        print(dp[W])


    elif N<=200 and mxv<=1000:
    #######################################################################
    # ナップサック
    # 重さ：max_wi,Wー10**9くらい
    # 価値：N*max_viー10**5くらい
    # dp[v]:v以上の価値となる最小の重さ
    #   dp[v]とdp[v-vi]+wi(i番目のアイテムをとる場合)　との小さいほうで更新
    #######################################################################
        max_vi = mxv
        max_V = N*max_vi
        dp = [W+1] * (max_V+1)
        dp[0] = 0
        dp = np.array(dp)
        for _ in range(N):
            w_, v_ = wv[_]
            dp[v_:] = np.minimum(dp[v_:], dp[:-v_] + w_)
    #    print(dp)
        print(np.max(np.where(dp <= W)))



if __name__ == '__main__':
    main()
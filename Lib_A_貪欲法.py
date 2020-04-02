####################
# 貪欲法
####################

def greedy(prices,values,budget):
    ind = list(range(len(price)))
    ind = sorted(ind, key=lambda x: values[x]/prices[x], reverse = True)
    psum = 0
    vsum = 0
    geti = []
    for i in ind:
        if psum + prices[i]>budget:
            break
        else:
            psum += prices[i]
            vsum += values[i]
            geti.append(i)
    return geti
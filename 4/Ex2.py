import scipy.special

def rank(T, n):
    k = len(T)
    rank = 0
    for i in range(0, k):
        for j in range(T[i-1]+1, T[i]):
            print(n-j)
            rank = rank + scipy.special.comb(n-j, k-i-1)
    print(rank)

rank([2,3,5], 5)
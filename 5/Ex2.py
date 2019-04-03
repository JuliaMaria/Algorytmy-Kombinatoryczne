import scipy.special

def rank(T):
    T = list(T)
    T.insert(0,0)
    k = len(T) - 1
    rank = 0
    for i in range(1, k+1):
        rank += scipy.special.binom(T[i]-1, k-i+1)
    print(int(rank))

rank([3, 2, 1])
rank([4, 2, 1])
rank([4, 3, 1])
rank([4, 3, 2])
rank([5, 2, 1])
rank([5, 3, 1])
rank([5, 3, 2])
rank([5, 4, 1])
rank([5, 4, 2])
rank([5, 4, 3])


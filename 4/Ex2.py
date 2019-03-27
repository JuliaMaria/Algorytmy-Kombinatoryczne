import scipy.special

def rank(T,n):
    T = list(T)
    T.insert(0,0)
    k = len(T) - 1
    rank = 0
    for i in range(1,k+1):
        for j in range((T[i-1]+1),(T[i]-1+1)):
            rank += int(scipy.special.binom((n-j),(k-i)))
    print(rank)

rank([1,2,3], 5)
rank([1,2,4], 5)
rank([1,2,5], 5)
rank([1,3,4], 5)
rank([1,3,5], 5)
rank([1,4,5], 5)
rank([2,3,4], 5)
rank([2,3,5], 5)
rank([2,4,5], 5)
rank([3,4,5], 5)




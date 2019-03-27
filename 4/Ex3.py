import scipy.special

def unrank(r,n,k):
    x = 1
    T = [0 for i in range(k+1)]
    for i in range(1,len(T)):
        while(scipy.special.binom(n-x,k-i)<=r):
            r = r - scipy.special.binom(n-x,k-i)
            x = x+1
        T[i] = x
        x = x + 1
    T.remove(0) 
    print(T)

unrank(0, 5, 3)
unrank(1, 5, 3)
unrank(2, 5, 3)
unrank(3, 5, 3)
unrank(4, 5, 3)
unrank(5, 5, 3)
unrank(6, 5, 3)
unrank(7, 5, 3)
unrank(8, 5, 3)
unrank(9, 5, 3)
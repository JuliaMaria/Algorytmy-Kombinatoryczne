def next(T, n):
    k = len(T)
    i = k-1
    while i >= 0:
        while T[i] == n-k+1+i:
            i = i-1
        T[i] = T[i] + 1
        add = 0
        for j in range(i+1, k):
            add = add + 1
            T[j] = T[i] + add
        i = i - 1
    print(T)

next([1,2,3], 5)
next([1,2,4], 5)
next([1,2,5], 5)
next([1,3,4], 5)
next([1,3,5], 5)
next([1,4,5], 5)
next([2,3,4], 5)
next([2,3,5], 5)
next([2,4,5], 5)
next([3,4,5], 5)
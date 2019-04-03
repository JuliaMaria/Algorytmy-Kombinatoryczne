def next(T, n):
    T = list(T)
    T.insert(0,0)
    k = len(T) - 1
    i=k
    while ((T[i-1]-T[i]==1) and (i!=1)):
        i=i-1
    T[i]=T[i]+1
    if (i!=k):
        T[i+1]=k-i
    for j in range(i+2,len(T)):
        T[j]=T[j-1]-1
    if(i==1 and T[1]==n+1):
        print("Ostatni element - brak nastepnika")
    else:
        T.remove(0)
        print(T)

next([3, 2, 1], 5)
next([4, 2, 1], 5)
next([4, 3, 1], 5)
next([4, 3, 2], 5)
next([5, 2, 1], 5)
next([5, 3, 1], 5)
next([5, 3, 2], 5)
next([5, 4, 1], 5)
next([5, 4, 2], 5)
next([5, 4, 3], 5)

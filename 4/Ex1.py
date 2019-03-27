def next(T, n):
	T = list(T)
	T.insert(0,0)
	k = len(T) - 1
	i = k
	while (T[i] == (n-k+i)):
		i = i-1
	if (i != 0):       
		T[i] = T[i] + 1
		for j in range(i+1,k+1):
			T[j] = T[j-1] + 1
		T.remove(0)
		print(T)
	else:
		print("Ostatni element - brak nastepnika")

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





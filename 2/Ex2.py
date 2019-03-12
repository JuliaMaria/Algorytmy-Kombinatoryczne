import numpy as np

def rank(subset, n): 

    result = np.repeat(0, n)

    for x in range(n):
        if x+1 in subset:
            result[x] = 1
    rank = 0  
    for x in range(n-1,-1,-1):
        power = n-(x+1)
        rank = rank + result[x]*np.power(2, power)
    print rank

rank([], 3)
rank([1], 3)
rank([1, 2], 3)
rank([1, 2, 3], 3)



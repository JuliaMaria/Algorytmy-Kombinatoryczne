import numpy as np

def rank(subset, n): 

    result = np.repeat(0, n)

    for x in range(n):
        if x+1 in subset:
            result[x] = 1
    b = 0
    r = 0  
    for x in range(0,n):
        b = (b+result[x])%2
        if b == 1:
            power = n-(x+1)
            r = r + np.power(2, power)
    print r

rank([], 3)
rank([3], 3)
rank([2, 3], 3)
rank([2], 3)
rank([1, 2], 3)
rank([1, 2, 3], 3)
rank([1, 3], 3)
rank([1], 3)

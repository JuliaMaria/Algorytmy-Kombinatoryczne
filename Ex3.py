import numpy as np

def generate(n, k): 
    if k == 0:
        return

    permutation = np.repeat(1, k)
    stop = np.repeat(n, k)

    while True: 
        x = k-1
        while permutation[x] >= n:
            x = x - 1
        permutation[x] = permutation[x] + 1
        x = x + 1
        while x < k:
            permutation[x] = 1
            x = x + 1
        ascending = True
        for i in range(0, k-1):
            if permutation[i] >= permutation[i+1]:
                ascending = False
        if ascending == True:
            print permutation
        if np.array_equal(permutation, stop):
            break

generate(5, 3) 
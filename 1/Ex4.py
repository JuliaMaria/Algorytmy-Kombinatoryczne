import numpy as np

def generate(n): 

    permutation = np.repeat(0, n)
    stop = np.repeat(1, n)

    while True: 
        x = n-1
        while permutation[x] >= 1:
            x = x - 1
        permutation[x] = permutation[x] + 1
        x = x + 1
        while x < n:
            permutation[x] = 0
            x = x + 1
        result = []
        for (idx, value) in enumerate(permutation):
            if value == 1:
                result.append(idx+1)
        print result
        if np.array_equal(permutation, stop):
            break

generate(3)

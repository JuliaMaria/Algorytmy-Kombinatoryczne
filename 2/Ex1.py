import numpy as np

def generate(n): 

    allPermutations = []

    permutation = np.repeat(0, n)
    allPermutations.append([])
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
        allPermutations.append(result)
        if np.array_equal(permutation, stop):
            break
    for i in range(n+1):
        for permutation in allPermutations:
            if len(permutation) == i:
                print permutation

generate(3)
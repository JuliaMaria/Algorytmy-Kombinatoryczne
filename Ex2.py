import numpy as np

def generate(k): 
    if k == 0:
        return

    permutation = np.repeat(1, k)
    print permutation
    stop = np.array(range(1, k+1))

    while True: 
        x = k-1
        while permutation[x] >= k:
            x = x - 1
        permutation[x] = permutation[x] + 1
        x = x + 1
        while x < k:
            permutation[x] = 1
            x = x + 1
        correct = True
        for i in range(0, k-1):
            if permutation[i] > i+1:
                correct = False
        if correct == True:
            print permutation
        if np.array_equal(permutation, stop):
            break

generate(3)
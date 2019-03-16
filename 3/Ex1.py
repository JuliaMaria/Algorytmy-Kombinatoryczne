import numpy as np

def generate(n): 

    start = np.repeat(0, n)
    stop = np.concatenate((np.array([1]), np.repeat(0, n-1)))

    while True: 
        count = 0
        for element in start:
            if element == 1:
                count = count + 1
        if count%2 == 0:
            start[n-1] = not start[n-1]
        else:
            x = n - 1
            while start[x] != 1:
                x = x - 1
            x = x - 1
            start[x] = not start[x]
        result = []
        for (idx, value) in enumerate(start):
            if value == 1:
                result.append(idx+1)
        print result
        if np.array_equal(start, stop):
            break

generate(3)
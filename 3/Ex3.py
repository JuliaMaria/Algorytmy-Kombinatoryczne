import numpy as np

def unrank(r, n): 

    result = np.repeat(0, n)
    bprev = 0
    for x in range(0, n):
        power = n-(x+1)
        b = r//np.power(2, power)
        r = r - np.power(2, power)*b
        if b != bprev:
            result[x] = 1
        bprev = b
    t = []
    for (idx, value) in enumerate(result):
        if value == 1:
            t.append(idx+1)  
    print t
    
unrank(0, 3)
unrank(1, 3)
unrank(2, 3)
unrank(3, 3)
unrank(4, 3)
unrank(5, 3)
unrank(6, 3)
unrank(7, 3)
import numpy as np

def unrank(r, n): 

    binary = format(r, "b")
    while len(binary) < n:
        binary = str(0)+binary
    binary = [int(i) for i in binary]
    result = []
    for (idx, value) in enumerate(binary):
        if value == 1:
            result.append(idx+1)
    print result
    

unrank(1, 3)
unrank(2, 3)
unrank(3, 3)
unrank(4, 3)



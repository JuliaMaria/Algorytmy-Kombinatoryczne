def generate(n, k): 
      
    permutation = range(1, n+1)
    permutation = "".join(str(x) for x in permutation)
    algorithm(permutation, "", n, k) 

def algorithm(set, element, n, k): 
      
    if (k == 0) : 
        print(element) 
        return

    for i in range(n):   
        newElement = element + set[i] 
        algorithm(set, newElement, n, k - 1) 

generate(5, 3) 
      
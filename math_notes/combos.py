
# calculate factoral:
fact = lambda n : 1 if n == 1 else n * fact(n-1) 

# non-repeating permutation:
def P(n, r): return (fact(n) / fact(n - r))  

# repeating permutation:
def rP(n, r): return (n ** r)  

# non-repeating combination: 
def C(n, r): return (fact(n) / (fact(r) * fact(n-r)))

# repeating combination: 
def rC(n, r): return (fact(n + r - 1) / (fact(r) * fact(n - 1)))


def new_set(num, id='id'):
    l = []
    for i in range(num): 
        l += { id + '_item_' + str(i) }
    return l


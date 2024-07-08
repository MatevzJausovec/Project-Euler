def get_primes(n):
    numbers = set(range(3,n,2))
    primes = [2]
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def getPermutations(array):
    if len(array) == 1:
        return [array]
    permutations = []
    for i in range(len(array)): 
        # get all perm's of subarray w/o current item
        perms = getPermutations(array[:i] + array[i+1:])  
        for p in perms:
            permutations.append([array[i], *p])
    return permutations

def stevke(n):
    list = []
    for _,x in enumerate(str(n)):
        list.append(int(x))
    return list

def stevilo(stevke):
    niz = ""
    for n in stevke:
        niz += str(n)
    return int(niz)

def cikli(prime):
    opcije = []
    for i in range(len(str(prime))):
        opcije.append(str(prime)[i] + str(prime)[i+1:] + str(prime)[:i])
    return opcije

def circular_primes_under(n=1000000):
    primes = get_primes(n)
    odg = 0
    x = 0
    for prime in primes:
        if x%1000 == 0:
            print(x//1000)
        x += 1
        """opcije"""
        opcije = []
        for i in range(len(str(prime))):
            opcije.append(str(prime)[i] + str(prime)[i+1:] + str(prime)[:i])
        test = True
        for cikel in opcije:
            permutirana_p = int(cikel)
            if not permutirana_p in primes:
                test = False
                break
        if test:
            odg += 1
    return odg

78521
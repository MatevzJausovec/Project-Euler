def get_primes(n):
    numbers = set(range(3,n,2))
    primes = [2]
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
        

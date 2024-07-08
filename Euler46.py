def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

def get_primes(n):
    numbers = set(range(3,n,2))
    primes = [2]
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def get_squares(n):
    out = []
    for i in range(1,n+1):
        out.append(i**2)
    return out

def search_under(n):
    primes = get_primes(n)
    
    for a in range(9,n+1,2):
        if a in primes:
            continue
        test = False
        for numb in range(1,a//4):
            if 2 * (numb**2) > a:
                break
            diff = a - 2 * (numb ** 2)
            if diff in primes:
                test = True
                break
        if not test:
            return a

    return "Fail"

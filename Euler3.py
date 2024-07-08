600851475143

def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

def factorisation(n):
    fact = []
    i = 2
    while i<=n:     
        if n%i==0:      
            fact.append(i)
            n//= i
        else:
            i=i+1
    return fact
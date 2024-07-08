def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)


def nth_prime(n):
    """
    This function finds the nth prime number.
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        if count == n:
            return num
        num += 1

def sum_prime_between(y,x):
    '''Enter only odd variable y'''
    sum = 0
    num = y
    if y < 3:
        sum += 2
    while num < x:
        if is_prime(num):
            sum = sum + num
        num += 2
    print(sum)
    print(num)
    print("FIN")

# sum_prime_between(1,500000)
# 9914236195
# 500001
    
import sys

# >>> sum_prime_between(1,2000000) 
# 142913828922
# 2000001
# FIN
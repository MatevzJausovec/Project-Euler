def sum_square(n, x=0):
    if n == x:
        return 0
    else:
        return n ** 2 +  sum_square(n - 1, x)
    
def square_sum(n, x=0):
    return ((n+1)*n//2)**2
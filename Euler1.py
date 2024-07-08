
def Sum_mult(n,a):
    if n <= 0:
        return 0
    return n - n%a + Sum_mult(n - n%a - a,a)


def Sum_3_5(n):
    return Sum_mult(n,3) + Sum_mult(n,5) - Sum_mult(n,15)


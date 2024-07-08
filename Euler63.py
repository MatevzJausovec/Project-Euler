# x^n < 10^n
# x < 10 in x^n > 10^(n-1)

def search():
    odg = 0
    for x in range(1,10):
        n = 1
        while x**n >= 10**(n - 1):
            odg += 1
            n += 1
    return odg

#49
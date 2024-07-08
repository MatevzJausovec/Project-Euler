def is_str_pnadigital(niz):
    if len(niz) != 9:
        return False
    for n in "123456789":
        if n not in niz:
            return False
    return True

def get_number(n):
    N = str(n)
    k = 2
    while len(N) < 9:
        N += str(n * k)
        k += 1
    return int(N)

# Začne z 9, do 9999

def search():
    n = 918273645
    for i in list(range(90,100)) + list(range(900,1000)) + list(range(9000,10000)):
        k = get_number(i)
        if is_str_pnadigital(str(k)):
            n = max(n,k)
    return n
        


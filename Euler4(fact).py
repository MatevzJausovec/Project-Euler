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


def find(a=9,b=5,c=9,k=999):
    if c < 0:
        c = 9
        b = b - 1
        if b < 0:
            b = 9
            c = c - 1
    Numb = 100001*a + 10010*b +1100*c

    if k < 990:
        return find(a,b,c - 1,999)
    elif Numb % k == 0:
        if (Numb // k) < 1000:
            print(Numb)
            print(k)
            return
        else:
            return find(a,b,c - 1,k)
    else:
        return find(a,b,c,k-1)

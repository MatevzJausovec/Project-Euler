def stevke(n):
    list = []
    for _,x in enumerate(str(n)):
        list.append(int(x))
    return list


def fakulteta(n):
    N = 1
    for i in range (1,n+1):
        N *= i
    return N

sum(stevke(fakulteta(100)))
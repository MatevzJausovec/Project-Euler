def zaporedje_e(n):
    odg = [2,1]
    for i in range(1,n//3 + 2):
        odg.append(2*i)
        odg.append(1)
        odg.append(1)
    return odg[:n]

def n_ti_pribl(n):
    st = 0
    im = 1
    nums = zaporedje_e(n)
    nums.reverse()
    for k in nums:
        st = st + k*im
        im, st = st, im
    im, st = st, im
    return(st, im)

def stevke(n=6963524437876961749120273824619538346438023188214475670667):
    list = []
    for _,x in enumerate(str(n)):
        list.append(int(x))
    return list

sum(stevke())
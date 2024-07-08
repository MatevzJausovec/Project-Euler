def stevke(n):
    sez =[]
    for _,x in enumerate(str(n)):
        sez.append(int(x))
    return sez

a = stevke(2 ** 1000)
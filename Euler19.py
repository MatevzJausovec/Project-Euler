# sundays <==> total_days//7 

# 1. jan 1901 == torek == 2

# koliko nedelj?

dnevi = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
dnevi_prestopno = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def search():    
    leto = 1901
    dan = 2
    stevilo = 0
    slovar = dnevi
    while leto <= 2000:
        if leto % 400 == 0:
            slovar = dnevi_prestopno
        elif leto % 100 == 0:
            slovar = dnevi
        elif leto % 4 == 0:
            """prestopno"""
            slovar = dnevi_prestopno
        else:
            """normalno"""
            slovar = dnevi

        for i in range(1,13):
            if dan % 7 == 0:
                stevilo += 1
            dan += slovar[i]
        leto += 1
    return stevilo


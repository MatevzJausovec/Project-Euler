def check_devisors(n):
    odg = []
    for i in range(1,n+1):
        if i in odg:
            break
        if n%i == 0:
            odg.append(i)
            odg.append(n//i)
    return odg

def triang_1st_numb_with_n_divisors():
    odg = 0
    i = 1
    while odg < 500:
        odg = len(check_devisors2(i*(i+1)//2))
        i += 1
        print(i), print(len(check_devisors(i*(i+1)//2)))
    return i*(i+1)//2

"try 2: bisection"

def triang_1st_numb_with_n_divisors_bisect(n):
    return

def triang(i):
    return i*(i+1)//2

def check_devisors2(n):
    odg = []
    for i in range(1,n+1):
        if i in odg:
            break
        if n%i == 0:
            odg.append(i)
            odg.append(n//i)
    return odg

# ODG: triang(12375)
# 76576500

# len(check_devisors(triang(i)))

# if len(odg) >= n:
#             print("test")
#             break
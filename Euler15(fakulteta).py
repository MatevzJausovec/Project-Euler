# levo / dol ==> oboje je lahko max 20
# permutacije 20a, 20b <==> 20 na 21 mest <==>
#
#
#
#
# fakulteta(40)//(fakulteta(20)**2)
# 137846528820
#
#
#

def fakulteta(n):
    x = 1
    for i in range(1,n+1):
        x *= i
    return x

def binom(n,r):
    return (fakulteta(n))//(fakulteta(r)*fakulteta(n - r))

# permut_s_ponaljanjem
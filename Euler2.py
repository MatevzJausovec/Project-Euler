def Fib(n,a=1,b=2):
    if n == 1:
        return a
    return Fib(n-1,b,a+b)

def Even_Fib_Sum(a,k):
    if Fib(a)> 4 * 10 ** 6:
        return k
    elif Fib(a)%2 == 0:
        return Even_Fib_Sum(a+1,k + Fib(a))
    return Even_Fib_Sum(a+1,k)
    
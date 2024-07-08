def next_collaz(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n + 1
    
def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = next_collaz(n)
        seq.append(n)
    return seq


"""od gor dol, preverim če je naslednji pod mil"""

def longest_under(n):
    numbers = set(range(1,n))
    max = 1
    odg = 1
    while numbers:
        p = numbers.pop()
        collatz = collatz_sequence(p)
        if len(collatz) >= max:
            odg = p
            max = len(collatz)
        numbers.difference_update(set(collatz))
    return odg


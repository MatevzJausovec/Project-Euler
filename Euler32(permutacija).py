# sum of all products, for wich A x B = C; A,B,C contain all digits 1-9 once
# * they must be of lenghts 2, 3, 4 to sum up to 9

def getPermutations(array):
    if len(array) == 1:
        return [array]
    permutations = []
    for i in range(len(array)): 
        # get all perm's of subarray w/o current item
        perms = getPermutations(array[:i] + array[i+1:])  
        for p in perms:
            permutations.append([array[i], *p])
    return permutations

def search_234():
    odg = set()
    permutations = getPermutations([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for permutation in permutations:
        A = 10*permutation[0] + permutation[1]
        B = 100*permutation[2] + 10*permutation[3] + permutation[4]
        C = 1000*permutation[5] + 100*permutation[6] + 10*permutation[7] + permutation[8]
        if A * B == C:
            odg.add(C)
    return odg

def search_144():
    odg = set()
    permutations = getPermutations([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for permutation in permutations:
        A = permutation[0]
        B = 1000* permutation[1] + 100*permutation[2] + 10*permutation[3] + permutation[4]
        C = 1000*permutation[5] + 100*permutation[6] + 10*permutation[7] + permutation[8]
        if A * B == C:
            odg.add(C)
    return odg

# print(sum(search_144() | search_234()))
# --> 45228



{5346, 5796, 6952, 7852, 4396, 7632, 7254}
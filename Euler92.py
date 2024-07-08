def stevke2(n):
    list = []
    for _,x in enumerate(str(n)):
        list.append(int(x)**2)
    return list

def next(n):
    list = []
    for _,x in enumerate(str(n)):
        list.append(int(x)**2)
    return sum(list)

def series(n):
    list = []
    m = n
    while not m in list:
        list.append(m)
        m = next(m)
    return list

# def search_under(n=10000000):
#     set1 = {1}
#     set89 = {89}
#     numbers = set(range(1,n + 1))
#     while numbers:
#         p = numbers.pop()
#         if p in set1 or p in set89:
#             continue
#         list_p = {p}
#         test = True
#         while test:
#             if next(p) in set1:
#                 set1 = set1.union(list_p)
#                 numbers.difference_update(list_p)
#                 test = False
#             elif next(p) in set89:
#                 set89 = set89.union(list_p)
#                 numbers.difference_update(list_p)
#                 test = False
#             else: 
#                 p = next(p)
#                 list_p.add(p)
    
    
#     return len(set89)

# def search_under2(n=10000000):
#     set1 = [1]
#     set89 = [89]
#     numbers = set(range(1,n + 1))
#     while numbers:
#         p = numbers.pop()
#         if p in set1 or p in set89:
#             continue
#         list_p = {p}
#         test = True
#         while test:
#             if next(p) in set1:
#                 set1 += list(list_p)
#                 numbers.difference_update(list_p)
#                 test = False
#             elif next(p) in set89:
#                 set89 += list(list_p)
#                 numbers.difference_update(list_p)
#                 test = False
#             else: 
#                 p = next(p)
#                 list_p.add(p)
    
    
#     return set89

def search_under3(n=10000000):
    set1 = []
    set89 = []
    for i in range(1,n + 1):
        if i%100000 == 0:
            print(i//100000, "%")
        list = series(i)
        if 1 in list:
            set1.append(i)
        if 89 in list:
            set89.append(i)
    return len(set89)

# 8581146
    

# def final(n=10000000):
#     s = 0
#     list89 = search_under2()
#     for k in range(1,n+1):
#         if k in list89:
#             s += 1
#             if s%100000 == 0:
#                 print(s)
#     return s


# print(1)
# print(search_under(10000))
# print(search_under2(10000))
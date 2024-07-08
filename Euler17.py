def seznam_stevk(n):
    if n % 1000 == 0:
        return print("Oh no")
    a3 = n//100
    a2 = n//10 - 10 * a3
    a1 = n%10
    return[a3,a2,a1]

def letters_in(n):
    """za števila manj ali enako 1000"""
    if n == 1000:
        return 11
    slovar_enic = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
    slovar_desetic = {0:0,2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
    najstke = {0:3, 1:6, 2:6, 3:8, 4:8, 5:7, 6:7, 7:9, 8:8, 9:8}
    """posebej za desetice"""
    """stotice isto kot enice + 'hundred and' --> 10"""
    seznam = seznam_stevk(n)
    k = 10
    if seznam[0] == 0:
        k = 0
    if seznam[1] == 0 and seznam[2] == 0:
        k = 7
    if seznam[1] == 1:
        return k + slovar_enic[seznam[0]] + najstke[seznam[2]]  
    else:
        return k + slovar_enic[seznam[0]] + slovar_desetic[seznam[1]] + slovar_enic[seznam[2]]
    
def letters_till_(n):
    sum = 0
    for i in range(1,n + 1):
        sum += letters_in(i)
    return sum

def e17():
    n1=(0,3,3,5,4,4,3,5,5,4)    # 1 to 9
    n10=(0,3,6,6,5,5,5,7,6,6)   # 10 to 90
    n11=(0,6,6,8,8,7,7,9,8,8)   # 11 to 19
    n=(7,10,11) # hundred, hundred and, one thousand

    n1to99x10 = (sum(n1)*9 + n10[1] + sum(n11) + sum(n10[2:])*10)*10 # from 1 to 99 all
    n100to900all = n[0]*9 + n[1]*99*9 + sum(n1)*100 # from 100 to 900

    print(n100to900all)
    
    letters = n1to99x10 + n100to900all + n[2]
    return letters

# 21124
#a + b + c = 1000
#
#a^2 + b^2 = c^2
#a*b*c = ?
# ==> a + b > c   ===> c < 500

import math

def Q_square(n):
    if  math.sqrt(n) % 1 == 0:
        return True
    else:
        return False
    
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True
    
def find():
   for a in range(1,1000):
      for b in range (a+1,1000):
         if Q_square(a**2 + b**2) == True and a + b + math.sqrt(a**2 + b**2) == 1000:
            print(a,b,"YES")
            break
   print("bad")

# 200 375 ---> 425
   
# 200*375*425 = 31875000
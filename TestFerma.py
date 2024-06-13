import math
import random

n = 2810864562635368426005268142616001

check = 0
osn = [0,0,0,0,0]

for i in  range (5):

    a = random.randint(2, n-2)
    r = pow(a, n - 1, n) 

    if r == 1:
        check = check + 1
        osn[i] = a
    else:
        print("\nЧисло n составное")
        print("Основание числа, для которого нарушается условие простоты: %d\n" %(a))  
        break
    
if check == 5:
    print("\nЧисло n, вероятно, простое")
    print("Основания 5 чисел, для которых выполняется условие простоты: \n %d\n %d\n %d\n %d\n %d\n" %(osn[0], osn[1], osn[2], osn[3], osn[4]))
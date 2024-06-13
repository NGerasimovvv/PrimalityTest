import math
import random

n = 2810864562635368426005268142616001

check = 0
osn = [0,0,0,0,0]

for i in range (5):

    s = 0
    r = n - 1
    while r % 2 == 0:
        s += 1
        r = r // 2

    a = random.randint(2, n - 2)

    y = pow(a, r, n)

    k = 0
    if (y != 1 and y != n - 1):
        
        j = 1
        
        
        while (j <= s - 1 and y != n - 1):

            y = pow(y, 2, n)

            if (y == 1):
                k = 1
                print('\nНарушено условие y != 1')
                print("Число n составное")
                print("Основание числа, для которого нарушается условие простоты: %d\n" %(a)) 
                break

            j += 1 

        if (k == 1):
            break

        if (y != n - 1):
                k = 1
                print('\nНарушено условие y == n - 1')
                print("Число n составное")
                print("Основание числа, для которого нарушается условие простоты: %d\n" %(a))
                break  
    
    if (k == 1):
        break
    
    check = check + 1
    osn[i] = a

if (check == 5):
    print("\nЧисло n, вероятно, простое")
    print("Основания 5 чисел, для которых выполняется условие простоты: \n %d\n %d\n %d\n %d\n %d\n " %(osn[0], osn[1], osn[2], osn[3], osn[4]))       

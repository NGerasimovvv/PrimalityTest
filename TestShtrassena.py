import math
import random

def SymbolJacobi(a,n):

    g = 1

    while 1:

        k = 0

        if a == 0:
            return 0

        if a == 1:
            return g

        while a % 2 == 0:

            k += 1
            a = a // 2

        if k % 2 != 0:
            if(((pow(n, 2) - 1) // 8) % 2 != 0):
                g = g * (-1)

        if a == 1:
            return g

        if (((a-1) // 2)*((n-1) // 2) % 2 != 0):
            g = g * (-1)

        a_temp = n % a
        n = a
        a = a_temp

n = 2810864562635368426005268142616001

check = 0
osn = [0,0,0,0,0]

for i in  range (5):

    a = random.randint(2, n-2)
    osn[i] = a
    r = pow(a, (n-1)//2, n)

    if (r != 1 and r != (n-1)):
        print('\nНарушено условие r == 1 and r == n - 1')
        print("Число n составное")
        print("Основание числа, для которого нарушается условие простоты: %d\n" %(a))
        break

    if (r == n - 1):
        r = -1

    s = SymbolJacobi(a,n)

    if (r != s):
        print('\nНарушено условие r == s')
        print("Число n составное")
        print("Основание числа, для которого нарушается условие простоты: %d\n" %(a)) 
        break
    else:
        check = check + 1
                
if (check == 5):
    print("\nЧисло n, вероятно, простое")
    print("Основания 5 чисел, для которых выполняется условие простоты: \n %d\n %d\n %d\n %d\n %d\n" %(osn[0], osn[1], osn[2], osn[3], osn[4]))
"""
Disclaimer: Este problema fue hecho a fuerza bruta porque
tuvimos la competición durante examenes y no hubo mucho tiempo.
Haciendo los calculos se veía fácil que el algoritmo simple
acababa en un tiempo razonable
"""

import japanese_numbers as jn
from itertools import permutations
from numba import jit


def all_permu(a):
    return set([''.join(p) for p in permutations(a)])

dic_ta = {}
dic_ta["一"]=1
dic_ta["二"]=2
dic_ta["三"]=3
dic_ta["四"]=4
dic_ta["五"]=5
dic_ta["六"]=6
dic_ta["七"]=7
dic_ta["八"]=8
dic_ta["九"]=9
dic_ta["十"]=10
dic_ta["百"]=100
dic_ta["千"]=1000
dic_ta["万"]=10000



A = ["一","二","三","四","五","六","七","八","九"]
B = ["十","百","千","万"]

@jit
def is_well_writen(a):

    flag = [0,0,0,0]
    B = ["十","百","千","万"]
    for i,e in enumerate(a):
        if e in ["十","百","千","万"]:
            if "万" == e:
                if sum(flag) > 0 or i == 0:
                    return False
                flag[3] = 1

            if e in ["十","百","千"] and i != 0:
                if a[i-1] in ["一"]:
                    return False

                for j,c in enumerate(["十","百","千"]):
                    if  e == c:
                        if sum(flag[:j+1]) > 0:
                            return False
                        flag[j] = 1



        elif i != 0:
            if a[i-1] in ["一","二","三","四","五","六","七","八","九"]:
                return False

    return True

@jit
def check(n,m,r):
    for n1 in n:
        for m1 in m:
            if n1+m1 in r:
                return "{} + {} = {}".format(n1,m1,n1+m1)
            elif n1*m1 in r:
                return "{} * {} = {}".format(n1,m1,n1*m1)
            elif n1-m1 in r:
                return "{} - {} = {}".format(n1,m1,n1-m1)



t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n,op, m,eq,r = [s for s in input().split(" ")]

        #print(n,m,r)
    n = [jn.to_arabic_numbers(a)[0] for a in all_permu(n) if is_well_writen(a)]
    n = [a for a in n if len(str(a)) <= 5]
    m = [jn.to_arabic_numbers(a)[0] for a in all_permu(m) if is_well_writen(a)]
    m = [a for a in m if len(str(a)) <= 5]
    r = [jn.to_arabic_numbers(a)[0] for a in all_permu(r) if is_well_writen(a)]
    r = [a for a in r if len(str(a)) <= 5]

    print("Case #{}: {}".format(i,check(n,m,r)))



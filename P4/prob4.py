import math
import numpy as np
from functools import reduce
def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a


def mcm(a,b):
  return a*b/mcd(a,b)

flatten = lambda l: [item for sublist in l for item in sublist]

t = int(input())  # read a line with a single integer

for i in range(1,t + 1):
  size = int(input())
  vec =  ([int(s) for s in input().split(" ")])
  vec.sort()
  dic = {}
  for p in vec:
    if p in dic.keys():
      dic[p] += 1
    else:
      dic[p] = 1
  x = []
  sol = 1
  for p in dic.keys():
    if dic[p]%p != 0:
        x.append(p/(mcd(dic[p]%p,p)))

  if x:
   sol = reduce( lambda x, y: mcm(x,y), x)
   sol = int(sol)

  num = sum( dic[p]/p*sol for p in dic.keys())
  b = mcd(len(vec)*sol, int(num))

  print("Case #{}: {}/{}".format(i, int(len(vec)*sol/b), int(num/b)))


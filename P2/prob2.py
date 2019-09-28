import math
import numpy
t = int(input())  # read a line with a single integer

def number_of_path( a, dic, mat ):
  if a == 'New Earth':
    return 1
  else:
    if a in mat.keys():
      return mat[a]
    else:
      mat[a] = numpy.sum([number_of_path(a,dic,mat) for a in dic[a] ])
      return mat[a]

for i in range(1, t + 1):
  p = int(input())  # read a line with a single integer
  dic = {}
  mat = {}
  for p in range(p):
    orig,d = [s for s in input().split(":")]
    dest = [s for s in d.split(",")]
    dic[orig]=[]
    for di in dest:
      dic[orig].append(di)

  print("Case #{}: {}".format(i, number_of_path('Galactica',dic,mat)))

import numpy as np
#vec =  ([int(s) for s in input().split(" ")])

def normalize(a,b):
  c=[l for l in a]
  d=[l for l in b]
  for i,l in enumerate(c):
    if l != b[i]:
      return [l,b[i]]

def to_int(a):
  return ord(a)-ord('a')

t = int(input())
for i in range(1,t + 1):

  n_letter = 0
  letter = []
  m = int(input())
  order=[]
  rules=[]


  for j in range(m):
    order.append(input())
 # print(order)

  for r in order:
    for a in r:
      if a not in letter:
        n_letter+=1
        letter.append(a)

  letter.sort(key=lambda x: to_int(x))
  ma = np.max([to_int(a) for a in letter])
  mat = np.zeros((ma+1,ma+1))

  for j in range(m-1):
    rules.append(normalize(order[j],order[j+1]))

  #print(rules)


  for r in rules:
    if r is not None:
      mat[to_int(r[0]),to_int(r[1])] = 1
  ###print(mat)


  for r in range(ma):
    mat = mat + np.matmul(mat,mat)

  mat = np.where( mat != 0, 1, mat)

  values = mat.sum(axis=1)

  guarda = True
  for y in range(len(letter)):
    if y not in values:
      guarda = False


  res = []
  values = np.dot(ma,np.ones(values.shape))-values

  for j,l in enumerate(letter):
    res.append( [l,values[to_int(l)]])

  letter.sort(key=lambda x : values[to_int(x)])

  if  guarda:
    print("Case #{}: {}".format(i, ' '.join(letter)))
  else:
    print("Case #{}: {}".format(i, 'AMBIGUOUS'))


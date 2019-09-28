import math
import numpy as np

def calculate_list(punches, f, h, w):
  results = []

  if f == 'T':
    #print('t')
    for p in punches:
      p1 = np.copy(p)
      p2 = np.copy(p)
      p1[1] += h
      #print('p1',p1)
      p2[1] = 2*h-1 - p1[1]
      #print('p2',p2)
      results.append(p1)
      results.append(p2)
    h = 2*h

  if f == 'R':
    #print('r')
    for p in punches:
      p1 = np.copy(p)
      p2 = np.copy(p)
      p2[0] = 2*w-1 - p1[0]
      results.append(p1)
      results.append(p2)
    w = 2*w

  if f == 'L':
    #print('l')
    for p in punches:
      p1 = np.copy(p)
      p2 = np.copy(p)
      p1[0] += w
      p2[0] = 2*w-1 - p1[0]
      results.append(p1)
      results.append(p2)
    w = 2*w


  if f == 'B':
    #print('b')
    for p in punches:
      p1 = np.copy(p)
      p2 = np.copy(p)
      p2[1] = 2*h-1 - p1[1]
      results.append(p1)
      results.append(p2)
    h = 2*h

  #print( 'H:',h )
  #print( 'W:',w )

  #print(results)
  return [results,h,w]








t = int(input())  # read a line with a single integer
#print(t)
for i in range(1, t + 1):
  W,H,F,P= [int(s) for s in input().split(" ")]
  fold = []
  punch = []
  for p in range(F):
    fold.append(input())


  for p in range(P):
    punch.append([int(s) for s in input().split(" ")])

  for f in fold:
    punch, H, W = calculate_list(punch, f, H, W)


  #print(punch)
  punch.sort(key=lambda x: x[0]*10**5+x[1])
  print("Case #{}:".format(i, i))
  for p in punch:
    print( p[0],p[1])

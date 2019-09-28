#vec =  ([int(s) for s in input().split(" ")])
t = int(input())  # read a line with a single integer

typewriter = [['1','2','3','4','5','6','7','8','9','0'],
              ['q','w','e','r','t','y','u','i','o','p'],
              ['a','s','d','f','g','h','j','k','l',';'],
              ['z','x','c','v','b','n','m',',','.','-']]

tw = [[a.upper() for a in sl]for sl in typewriter ]

def fi(a):
  for i in range(4):
    if a in tw[i]:
      return i

def si(a):
  return tw[fi(a)].index(a)


def offset(a,b):
  return [fi(a)-fi(b),si(a)-si(b)]

for i in range(1,t + 1):
  p = input()

  frase = input()
  coded_p = frase[len(frase)-1]

  os = offset(p,coded_p)

  msg = ""

  for l in frase:
    if l == ' ':
      msg = msg + ' '
    else:
      f = fi(l)
      s = si(l)
      msg = msg + tw[(f+os[0])%4][(s+os[1])%10]

  print("Case #{}: {}".format(i, msg))


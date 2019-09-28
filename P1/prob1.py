import math
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  # print(n,m)
  n = math.ceil(n/2)
  m = math.ceil(m/2)
  print("Case #{}: {}".format(i, n+m))
  # check out .format's specification for more formatting options

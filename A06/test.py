N, Q = input().split()
Arrivals = list(map(int, input().split()))
pair = []
for q in range(int(Q)):
  pair.append(list(map(int, input().split())))

for p in pair:
  sum = 0
  for i in range(p[0], p[1]+1):
    sum += Arrivals[i-1]
  print(sum)


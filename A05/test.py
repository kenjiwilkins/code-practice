inputs = input().split()
N = int(inputs[0])
K = int(inputs[1])
found = 0
for x in range (1, N+1):
  for y in range (1, N+1):
    if x+y >= K:
      break
    elif K - x - y <= N:
      found += 1

print(found)
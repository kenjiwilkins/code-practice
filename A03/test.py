input1 = input().split()
N = int(input1[0])
K = int(input1[1])
arrayP = list(map(lambda n:int(n)-K, input().split()))
arrayQ = list(map(int, input().split()))

for i in arrayQ:
  for j in arrayP:
    if i + j == 0:
      print("Yes")
      exit()

print("No")
input1 = input().split()
N = int(input1[0])
X = int(input1[1])
input2 = input().split()
A = [int(i) for i in input2]
for i in A:
  if i == X:
    print("Yes")
    exit()

print("No")
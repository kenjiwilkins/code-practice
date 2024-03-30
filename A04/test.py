N = int(input())
binary = "{0:b}".format(N)
length = len(binary)
print(("0" * (10-length)) + str(binary))
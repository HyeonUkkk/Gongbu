import math
n = input()
l = list(map(int,input().split()))
array = [True for i in range(max(l)+1)]
array[:1] = [False,False]
for i in range(2, int(math.sqrt(max(l)))+1):
    if i :
        j = 2
        while i * j <= max(l):
            array[i*j] = False
            j += 1
print(len([i for i in l if array[i]]))

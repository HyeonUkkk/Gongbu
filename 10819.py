import sys
import itertools
n = int(input())
l = map(int,input().split())
Maxvalue = float("-inf") 
for i in itertools.permutations(l,n):
    i = list(i)
    a= 0
    for j in range(0,n-1):
        a += abs(i[j]-i[j+1])
    Maxvalue = max(Maxvalue,a)
print(Maxvalue)

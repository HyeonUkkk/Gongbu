import sys
import itertools
input=sys.stdin.readline
l = [int(input()) for i in range(9)]
l = itertools.combinations(l,7)
for i in l:
    if sum(i)==100:
        print(*sorted(i),sep='\n')
        break

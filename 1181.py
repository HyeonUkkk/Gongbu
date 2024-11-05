import sys
input=sys.stdin.readline
print(*sorted(sorted(list(set([input() for i in range(int(input()))]))),key=len),sep='')

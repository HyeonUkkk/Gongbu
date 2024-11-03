import sys
l = [ sys.stdin.readline() for i in range(int(input()))]
print(*sorted(map(int,l)),sep='\n')

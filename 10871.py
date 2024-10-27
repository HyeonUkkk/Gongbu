a, n = map(int,input().split())
print(*[i for i in [l for l in map(int,input().split())] if i<n])

import sys
l = [0] * 10001
for i in range(int(input())):
    l[int(sys.stdin.readline())] +=1
for i in range(len(l)):
    for j in range(l[i]):
        print(i)
 
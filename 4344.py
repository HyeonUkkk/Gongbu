for i in range(int(input())):
    n,*l=map(int,input().split())
    print(f"{round((list(map(lambda x : x > sum(l)/n,l)).count(1)/n)*100,3):.3f}%")

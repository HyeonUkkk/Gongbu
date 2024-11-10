def cutwood(length):
    ans = 0
    for i in l:
        if i>=length:
            ans += i-length
    return ans
def binarysearch(high,low):
    global m
    while 1:
        mid = (low + high) // 2
        if low + 1 >= high:
            break
        if m>cutwood(mid):
            high = mid
        else:
            low = mid
    return mid

if __name__ == "__main__":
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    print(binarysearch(1000000000,0))

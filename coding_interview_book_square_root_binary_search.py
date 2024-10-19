def square_root(n):
    start = 1
    end = n

    while start <= end:
        mid = (start+end)//2
        if mid*mid == n:
            return mid
        elif mid*mid > n:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1

res = square_root(n=1024)
print(res)
#n=1024 res=32
#n=100 res=10
#n=64 res=8
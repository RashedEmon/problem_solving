arr = [1,3,4,5,6,7,10, 15]
t = 2
def binary_search(t, arr):
    l = 0
    r = len(arr)-1
    while l < r:
        m=(l+r)//2
        print(l, m, r)
        if t == arr[m]:
            return m
        if t > arr[m]:
            l = m + 1
        else:
            r = m - 1
    return r+1

print(binary_search(t , arr))



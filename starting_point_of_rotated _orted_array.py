# To find min value in roated sorted array.
# Or To find where rotation happened.
# find starting point of roated sorted array.


arr = [5,6,7,8,1,2,3,4]
l = 0
r = len(arr)-1
while l < r:
    m=(l+r)//2
    print(l, m, r)
    if arr[m] > arr[r]:
        l = m + 1
    else:
        r = m

print(r)

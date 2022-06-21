#find upper and lower index of a target value from array.
#binary search concept is used to solve this problem in O(log(n)) complexity.

arr = [1,2,2,3,3,5,5,5,5,5,5,7,9,9,9,10]

def lower_bound(arr,target):
    l = 0
    r = len(arr)-1
    
    while(l<=r):
        m = (l+r)//2
        if arr[m] < target:
            l = m+1
        elif arr[m] > target:
            r = m-1
        else:
            if m == 0:
                return 0
            if arr[m-1] < arr[m]:
                return m
            else:
                r = m-1
    return -1
    

def upper_bound(arr,target):
    l = 0
    r = len(arr)-1
    
    while(l<=r):
        m = (l+r)//2
        if arr[m] < target:
            l = m+1
        elif arr[m] > target:
            r = m-1
        else:
            if m == len(arr)-1:
                return m
            if arr[m+1] > arr[m]:
                return m
            else:
                l = m+1
    return -1
print([lower_bound(arr,5),upper_bound(arr,5)])


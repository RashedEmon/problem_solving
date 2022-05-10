# find expected index for an element to place in the array. 
def solve(arr,target):
    mid=0
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return mid+1
    
if __name__ == "__main__":
    print(solve([1,2,3,6,7,9,10],5))

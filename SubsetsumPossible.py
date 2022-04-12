#this function determine is subset possible for given input or not.
def isSubsetsumPossible(arr,i,w):
    if w<0:
        return False
    if w == 0:
        return True
    if i>=len(arr):
        return False
    
    a=isSubsetsumPossible(arr,i+1,w-arr[i])
    b=isSubsetsumPossible(arr,i+1,w)
    return a or b

if __name__ == "__main__":
    arr=[5,15,3,17,12]
    w=50
    print(isSubsetsumPossible(arr,0,w))

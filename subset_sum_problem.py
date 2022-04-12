def subsetsum(arr,i,w):
    if w<0:
        return 0
    if w == 0:
        return 1
    if i>=len(arr):
        return 0
    
    a=subsetsum(arr,i+1,w-arr[i])
    b=subsetsum(arr,i+1,w)
    return a+b

if __name__ == "__main__":
    arr=[5,15,3,17,12]
    w=20
    print(subsetsum(arr,0,w))

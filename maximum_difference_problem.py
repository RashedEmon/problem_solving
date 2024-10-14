#Maximum Difference Problem
arr = [2,3,51,6,3,1,2,100]

mn = arr[0]
res = float('-inf')

for i in range(1, len(arr)):
    if mn > arr[i]:
        mn = arr[i]
    else:
        res = max(arr[i]-mn, res)

print(res)

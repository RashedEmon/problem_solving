class Solution:
    def binarySearch(self,arr,left,right,target):
        while left <= right:
            mid = (left+right)//2
            if arr[mid]<target:
                left=mid+1
            elif arr[mid]>target:
                right=mid-1
            else:
                return mid+1
        return -1

    def solve(self,arr,target):
        n=len(arr)-1
        for i in range(len(arr)):
            a=self.binarySearch(arr,i,n,target-arr[i])
            
            if a==i+1:
                a=self.binarySearch(arr,i+1,n,target-arr[i])
                
            if a != -1:
                break

        return [i+1,a]
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.solve(numbers,target)

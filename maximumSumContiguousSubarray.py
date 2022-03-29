import math
def maxSumContSub(nums):
    maxi=-math.inf
    sum=0
    for number in nums:
        sum+=number
        if sum>maxi:
            maxi=sum
    return maxi
if __name__ == "__main__":
    print(maxSumContSub([5,5,-7,-8,1,9]))

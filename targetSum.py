
#target sum from a list of number
#determine the number of sequences made from a list of numbers and print the combinations as list

# input: [1,2,3,5,6,7,8]
# output: 5
#         ['127', '136', '235', '28', '37']

arr=[1,2,3,5,6,7,8]
result=[]
def solve(target:int,sum:int,index:int,count:int, osf:str)->int:
    if(sum==target):
        result.append(osf)
        return count+1
    if(index>=len(arr) or sum>target):
        return 0
    a=solve(target,sum+arr[index],index+1,count,f'{osf}{arr[index]}')
    b=solve(target,sum,index+1,count,osf)
    
    return a+b
    
if __name__=="__main__":
    res=solve(10,0,0,0,'')
    print(res)
    print(result)

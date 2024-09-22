#all path printing
# arr=[]
# def solve(n:int,osf:str):
#     if n==0:
#         arr.append(osf)
#         return
#     if n<0:
#         return
#     solve(n-1,f'{1}{osf}')
#     solve(n-2,f'{2}{osf}')
#     solve(n-3,f'{3}{osf}')
#     return

#without memoization
# def solve(n:int)->int:
#     if n==0:
#         return 1;
#     if n<0:
#         return 0;
#     else:
#         return solve(n-1)+solve(n-2)+solve(n-3)
        
        
#with memoization
#arr=[ -1 for _ in range(0,100)]
# def solve(n:int)->int:
#     if n==0:
#         return 1;
#     if n<0:
#         return 0;
#     if arr[n] != -1:
#         return arr[n]
#     else:
#         arr[n]=solve(n-1)+solve(n-2)+solve(n-3)
#         return arr[n]

#minimum step to go destination
# arr=[]
# def minstair(target:int, n:int,i:int,osf:str)->int:
#     if n==target:
#         arr.append(osf)
#         return i;
#     if n>target:
#         return 10000;
        
#     a=minstair(target,n+1,i+1,f'{osf}{1}')
#     b=minstair(target,n+2,i+1,f'{osf}{2}')
#     c=minstair(target,n+3,i+1,f'{osf}{3}')
    
#     return min(a,b,c)

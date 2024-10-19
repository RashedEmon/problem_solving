
def power(a,n):
    

    def dfs(a, n):
        if n==1:
            return a
        
        res = power(a, n/2)

        return res*res
    
    if n%2 == 1 and n > 1:
        n = n-1
        return a*dfs(a, n)
    return dfs(a, n)

a = 2
n = 64
res = power(a, n)
print(res)
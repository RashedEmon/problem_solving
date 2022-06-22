#leetcode #medium #stack
s = "3[A2[C]]2[programmer3[Emon]]"
arr = [i for i in s]

stack = []
for i in range(len(arr)):
    
    if arr[i] == ']':
        temp=""
        number=""
        while(stack[-1] != '['):
            temp=stack.pop()+temp
        stack.pop()
        while(stack[-1] >= '0' and stack[-1] <= '9'):
            number=stack.pop()+number
            if len(stack)<=0:
                break
        
        if len(number) == 0:
            number=1
        else:
            number=int(number)
        for i in number*temp:
            stack.append(i)
        number=""
        temp=""
    else:
        stack.append(arr[i])
print("".join(stack))

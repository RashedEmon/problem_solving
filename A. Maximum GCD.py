#codeforces #math #800
t = int(input())

for _ in range(t):
    n = int(input())
    a = pow(2, n)
    b = pow(2, n//2)-2

    print((a+b)-(a-2-b))

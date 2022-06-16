#codeforces #Greedy #800
t = int(input())

for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))

    b = list(map(int, input().split()))

    mina = min(a)
    minb = min(b)
    # print(mina, minb)
    ans = 0
    for i in range(0, n):
        ans += max(a[i]-mina, b[i]-minb)

    print(ans)

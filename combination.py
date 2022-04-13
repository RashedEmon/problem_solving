def combination(n, r):
    if n == r or r == 0:
        return 1
    if r > n:
        return 0
    if n == 0:
        return 0

    return combination(n-1, r-1) + combination(n-1, r)


print(combination(3, 2))

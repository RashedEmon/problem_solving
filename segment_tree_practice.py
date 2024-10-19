arr = [0,1,2,3,4,5,6,7,8,9,10]
tree = [float('inf')]*len(arr)*3

#                    [1,2,3,4,5,6,7,8,9]
#           [1,2,3,4]                [5,6,7,8,9]
#    [1,2]        [3, 4]      [5,6]            [7,8,9]
#  [1]   [2]     [3]  [4]   [5]   [6]        [8]  [8,9]
#                                                [8]  [9]

def init(node, f, l):
    if f==l:
        tree[node] = arr[f]
        return
    left = node*2
    right = node*2 + 1
    mid = (f+l)//2

    init(left, f, mid)
    init(right, mid+1, l)

    tree[node] = tree[left] + tree[right]

init(1, 1, len(arr)-1)

def query(node, b, e, i, j):
    if j < b or i > e:
        return 0
    
    if i <= b and j >= e:
        return tree[node]
    
    left = node*2
    right = node*2 + 1
    mid = (b+e)//2

    ls = query(left, b, mid, i, j)
    rs = query(right, mid+1, e, i, j)
    return ls+rs


res = query(1, 1, len(arr) - 1, 3, 9)
print(res)


def update(node, b, e, i, value):
    
    if i < b or  e < i:
        return tree[node]

    if i == b and i == e:
        tree[node] = value
        return value
    
    left = node*2
    right = node*2 + 1
    mid = (b+e)//2

    update(left, b, mid, i, value)
    update(right, mid+1, e, i, value)

    tree[node] = tree[left] + tree[right]

update(1,1,len(arr)-1, 9, 20)

print(tree)

res = query(1, 1, len(arr) - 1, 2, 6)
print(res)

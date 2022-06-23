#this script calculates the minimum distances of a node from root node using dfs.
def solve(tree, root, distance,i):
    distance[root] = i
    if len(tree[root]) <= 0:
        return
    for node in tree[root]:
        solve(tree,node,distance,i+1)
    

n = int(input())
tree = {}
for i in range(1,n+1):
    tree[i] = []
for i in range(1,n):
    a,b = [int(item) for item in input().split()]
    if a in tree:
        tree[a]+=[b]
    else:
        tree[a] = [b]

distance = [0 for i in range(0,n+1)]
solve(tree, 1 , distance, 0)
print(distance)

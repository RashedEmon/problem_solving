def solve(maze, i, j, n, s, visited):
    if i == n-1 and j == n-1:
        print(s)
        return
    if i > n-1 or j > n-1 or i < 0 or j < 0:
        return

    if maze[i][j] == 0:
        return

    if visited[i][j] == True:
        return

    visited[i][j] = True
    solve(maze, i, j+1, n, f"{s}R", visited)
    solve(maze, i, j-1, n, f"{s}L", visited)
    solve(maze, i-1, j, n, f"{s}U", visited)
    solve(maze, i+1, j, n, f"{s}D", visited)
    visited[i][j] = False
    s = s[:-1]
    return


if __name__ == "__main__":
    n = 4
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]]
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    solve(maze, 0, 0, n, "", visited)

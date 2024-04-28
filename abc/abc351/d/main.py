# func
from collections import deque

def bfs(matrix, start):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque([start])
    visited[start[0]][start[1]] = True
    result = []

    while queue:
        row, col = queue.popleft()
        result.append((row, col))
        
        for c_x, c_y in directions:
            c_row, c_col = row + c_x, col + c_y
            if 0 <= c_row < rows and 0 <= c_col < cols:
                if matrix[c_row][c_col] == '#':
                    continue


        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if not visited[new_row][new_col] and matrix[new_row][new_col]:
                        queue.append((new_row, new_col))
                        visited[new_row][new_col] = True

    return len(result)


# input
H, W = map(int, input().split())
grid = []
for i in range(H):
    grid.append(list(input()))

# solve
ans = -1
for i in range(H):
    for j in range(W):
        x = bfs(grid, [i, j])
        ans = max(ans, x)
# answer
print(ans)

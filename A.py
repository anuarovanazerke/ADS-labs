from collections import deque

def marios_war(grid, m, n):
    queue = deque()
    mushrooms = 0 
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0)) 
            elif grid[i][j] == 1:
                mushrooms += 1
    
    if mushrooms == 0:
        return 0
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    max_minutes = 0
    while queue:
        x, y, minutes = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = 2 
                mushrooms -= 1
                queue.append((nx, ny, minutes + 1))
                max_minutes = max(max_minutes, minutes + 1)
    
    return max_minutes if mushrooms == 0 else -1

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

print(marios_war(grid, m, n))

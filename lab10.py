#A
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n;
    cin >> m >> n;
    vector<vector<int>> grid(m, vector<int>(n));
    queue<pair<int,int>> q;
    int mushrooms = 0;

    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            cin >> grid[i][j];
            if(grid[i][j] == 2)
                q.push({i,j});
            else if(grid[i][j] == 1)
                mushrooms++;
        }
    }

    if(mushrooms == 0){
        cout << 0 << "\n";
        return 0;
    }

    vector<pair<int,int>> directions = {{-1,0},{1,0},{0,-1},{0,1}};
    int minutes = 0;

    while(!q.empty()){
        int size = q.size();
        for(int i = 0; i < size; i++){
            auto [x, y] = q.front();
            q.pop();
            for(auto [dx, dy] : directions){
                int nx = x + dx, ny = y + dy;
                if(nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1){
                    grid[nx][ny] = 2;
                    mushrooms--;
                    q.push({nx, ny});
                }
            }
        }
        minutes++;
    }

    if(mushrooms > 0)
        cout << -1 << "\n";
    else
        cout << minutes - 1 << "\n"; 
    return 0;
}

#B
from collections import deque
import sys
input = sys.stdin.readline
def shortest_path(n, adj_matrix, start, end):
    visited = [False] * n
    queue = deque()
    queue.append((start, 0))
    visited[start] = True
    
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))
    
    return -1 
n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]
start, end = map(int, input().split())
print(shortest_path(n, adj_matrix, start - 1, end - 1))

#C
def min_operations(n, m):
    path = []
    
    while m > n:
        path.append(m)
        if m % 2 == 0:
            m //= 2
        else:
            m += 1
    while n > m:
        path.append(m)
        m += 1
    
    path.append(n)
    path.reverse()
    result = []
    current = n
    for x in path[1:]:
        result.append(x)
    
    return len(result), result
n, m = map(int, input().split())
ops, seq = min_operations(n, m)

print(ops)
if ops > 0:
    print(' '.join(map(str, seq)))

#D


#E
import sys
def solve():
    n, q = map(int, sys.stdin.readline().split())
    a = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        a.append(row)
    
    for _ in range(q):
        line = sys.stdin.readline().split()
        elems = [int(x)-1 for x in line]
        ok = True
        k = len(elems)
        for i in range(k):
            if not ok:
                break
            for j in range(i+1, k):
                if a[elems[i]][elems[j]] == 0:
                    ok = False
                    break
        print("YES" if ok else "NO")
if __name__ == "__main__":
    solve()

#F
import sys
sys.setrecursionlimit(10**7)
def solve():
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    m = int(data[1])

    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
    index = 2
    for _ in range(m):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        union(x, y)
    s = int(data[index])
    f = int(data[index + 1])
    print("YES" if find(s) == find(f) else "NO")
if __name__ == "__main__":
    solve()
#G
import sys
sys.setrecursionlimit(10**7)
from collections import deque
def solve():
    data = sys.stdin.readline().split()
    n, m = map(int, data)
    g = [[] for _ in range(n + 1)]
    edges = []  
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        g[u].append(v)
        edges.append((u, v))

    color = [0] * (n + 1)
    parent = [-1] * (n + 1)
    cycle = []
    def dfs(u):
        nonlocal cycle
        color[u] = 1
        for v in g[u]:
            if color[v] == 0:
                parent[v] = u
                if dfs(v):
                    return True
            elif color[v] == 1:
                cycle = []
                cur = u
                cycle.append((u, v))
                while cur != v:
                    p = parent[cur]
                    cycle.append((p, cur))
                    cur = p
                return True
        color[u] = 2
        return False
    for i in range(1, n + 1):
        if color[i] == 0 and dfs(i):
            break

    if not cycle:
        print("YES")
        return

    def is_dag_without(edge_to_remove):
        u0, v0 = edge_to_remove
        indeg = [0] * (n + 1)

        for u in range(1, n + 1):
            for v in g[u]:
                if u == u0 and v == v0:
                    continue
                indeg[v] += 1
        q = deque()
        for i in range(1, n + 1):
            if indeg[i] == 0:
                q.append(i)
        visited_count = 0
        while q:
            u = q.popleft()
            visited_count += 1
            for v in g[u]:
                if u == u0 and v == v0:
                    continue
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return visited_count == n
    for e in cycle:
        if is_dag_without(e):
            print("YES")
            return
    print("NO")
if __name__ == "__main__":
    solve()

#H
from collections import deque
import sys
def solve():
    line = sys.stdin.readline().strip()
    if not line:
        return
    n, m = map(int, line.split())
    grid = []
    for _ in range(n):
        row = sys.stdin.readline().strip()
        row = row[:m]
        grid.append(list(row))

    visited = [[False] * m for _ in range(n)]

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited[sr][sc] = True

        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if not visited[nr][nc] and grid[nr][nc] == '1':
                        visited[nr][nc] = True
                        q.append((nr, nc))
    islands = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and not visited[i][j]:
                islands += 1
                bfs(i, j)
    print(islands)
if __name__ == "__main__":
    solve()

#J
import sys
from collections import defaultdict, deque
def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = defaultdict(list)
    for _ in range(m):
        x = int(next(it)); y = int(next(it))
        g[x].append(y)
        g[y].append(x)

    visited = [False] * (n + 1)
    bigfam_count = 0

    for v in range(1, n + 1):
        if visited[v]:
            continue
        comp = []
        q = deque([v])
        visited[v] = True
        comp.append(v)

        while q:
            u = q.popleft()
            for nei in g[u]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)
                    comp.append(nei)
        root = min(comp)
        parent = {root: None}
        children_count = defaultdict(int)

        q = deque([root])
        seen = set([root])
        while q:
            u = q.popleft()
            for nei in g[u]:
                if nei not in seen:
                    seen.add(nei)
                    parent[nei] = u
                    children_count[u] += 1
                    q.append(nei)
        for node in comp:
            if node == root:
                bigfam_count += 1
            else:
                p = parent.get(node)
                if p is not None and children_count[node] > children_count[p]:
                    bigfam_count += 1
    print(bigfam_count)
if __name__ == "__main__":
    solve()

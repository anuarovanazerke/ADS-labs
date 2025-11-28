#A
import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())
events = [[] for _ in range(N + 2)] 
ends   = [[] for _ in range(N + 2)]   

for sid in range(M):
    l, r, c = map(int, input().split())
    events[l].append((c, r, sid))
    ends[r].append(sid)

active = []    
deleted = set() 
answer = 0

for i in range(1, N):

    for c, r, sid in events[i]:
        heapq.heappush(active, (c, r, sid))
    for sid in ends[i]:
        deleted.add(sid)
    while active and active[0][2] in deleted:
        heapq.heappop(active)

    c, r, sid = active[0]
    answer += c

print(answer)

#B
n = int(input())
a = list(map(int, input().split()))
total = sum(a)
m = min(a)

print(total + (n - 2) * m)

#C
import sys

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        ra = self.find(a); rb = self.find(b)
        if ra == rb:
            return False
        if self.r[ra] < self.r[rb]:
            self.p[ra] = rb
        elif self.r[rb] < self.r[ra]:
            self.p[rb] = ra
        else:
            self.p[rb] = ra
            self.r[ra] += 1
        return True

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        return
    m = int(next(it))
    A = int(next(it))
    B = int(next(it))
    edges = []
    for _ in range(m):
        typ = next(it)
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        L = int(next(it))
        if typ == "big":
            cost_per_km = A
        elif typ == "small":
            cost_per_km = B
        else:  # "both"
            cost_per_km = min(A, B)
        w = cost_per_km * L
        edges.append((w, u, v))
    edges.sort(key=lambda x: x[0])
    dsu = DSU(n)
    total = 0
    used = 0
    for w, u, v in edges:
        if dsu.union(u, v):
            total += w
            used += 1
            if used == n - 1:
                break
    if n == 0 or used != n - 1:
        print("impossible")
    else:
        print(total)

if __name__ == "__main__":
    main()
#D
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            self.p[a] = b
        elif self.r[b] < self.r[a]:
            self.p[b] = a
        else:
            self.p[b] = a
            self.r[a] += 1
        return True

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
edges = []

for i in range(n):
    for j in range(i + 1, n):
        if mat[i][j] == 0:
            edges.append((0, i, j))
        else:
            edges.append((mat[i][j], i, j))

edges.sort()
dsu = DSU(n)
ans = 0
used = 0
for w, u, v in edges:
    if dsu.union(u, v):
        ans += w
        used += 1
        if used == n - 1:
            break

print(ans)

#E
import sys
sys.setrecursionlimit(10**7)

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            self.p[a] = b
        elif self.r[b] < self.r[a]:
            self.p[b] = a
        else:
            self.p[b] = a
            self.r[a] += 1
        return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    dsu = DSU(n+1)
    active = [False] * (n+1)
    components = 0
    answer = [0] * (n+2)
    for v in range(n, 0, -1):
        active[v] = True
        components += 1
        for u in adj[v]:
            if active[u]:
                if dsu.union(u, v):
                    components -= 1
        answer[v] = components
    out_lines = []
    for k in range(1, n+1):
        if k == n:
            out_lines.append("0")
        else:
            out_lines.append(str(answer[k+1]))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()

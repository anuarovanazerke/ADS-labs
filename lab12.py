#A
#B
#C
#D
#E
import sys
def find_negative_cycle(n, mat, NOEDGE=100000):
    edges = []
    for i in range(n):
        for j in range(n):
            w = mat[i][j]
            if w != NOEDGE:
                edges.append((i, j, w))

    
    dist = [0] * n
    parent = [-1] * n

    x = -1  
    for it in range(n):
        x = -1
        for (u, v, w) in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                x = v
       
    if x == -1:
        return None  

    for _ in range(n):
        x = parent[x]

    cycle = []
    v = x
    while True:
        cycle.append(v)
        v = parent[v]
        if v == x:
            break
    cycle.reverse()
    cycle_nodes = [c + 1 for c in cycle]  
    cycle_nodes.append(cycle_nodes[0])     

    return cycle_nodes

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    mat = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            try:
                mat[i][j] = next(it)
            except StopIteration:
                mat[i][j] = 100000 
    res = find_negative_cycle(n, mat, NOEDGE=100000)
    if res is None:
        print("NO")
    else:
        print("YES")
        print(len(res))
        print(" ".join(map(str, res)))

if __name__ == "__main__":
    main()

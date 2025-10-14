#A
import sys
input=sys.stdin.readline
def solve():
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    paths=[input().strip() for r in range(m)]
    tree=[[val,None,None] for val in arr]
    root=0
    for i in range(1,n):
        node=root
        while True:
            if arr[i]<tree[node][0]:
                if tree[node][1] is None:
                    tree[node][1]=i
                    break
                node=tree[node][1]
            else:
                if tree[node][2] is None:
                    tree[node][2]=i
                    break
                node=tree[node][2]
    for path in paths:
        node=root
        ok=True
        for c in path:
            if node is None:
                ok=False

                break
            node=tree[node][1] if c=='L' else tree[node][2]
        if node is None:
            ok=False
        print("YES" if ok else "NO")
if __name__=="__main__":
    solve()
#B
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def find_node(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    elif target < root.val:
        return find_node(root.left, target)
    else:
        return find_node(root.right, target)


def subtree_size(node):
    if node is None:
        return 0
    return 1 + subtree_size(node.left) + subtree_size(node.right)


n = int(input().strip())
values = list(map(int, input().split()))
target = int(input().strip())

root = None
for v in values:
    root = insert(root, v)
node = find_node(root, target)

print(subtree_size(node))

#C
#D
#E
from collections import deque, defaultdict
n = int(input().strip())

children = defaultdict(lambda: [None, None]) 
for _ in range(n - 1):
    x, y, z = map(int, input().split())
    if z == 0:
        children[x][0] = y
    else:
        children[x][1] = y

q = deque([1]) 
max_width = 0
while q:
    level_size = len(q)
    max_width = max(max_width, level_size)
    for _ in range(level_size):
        node = q.popleft()
        left, right = children[node]
        if left:
            q.append(left)
        if right:
            q.append(right)

print(max_width)

#F
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def count_triangles(node):
    if node is None:
        return 0
    count = 0
    if node.left and node.right: 
        count += 1
    count += count_triangles(node.left)
    count += count_triangles(node.right)
    return count

n = int(input().strip())
values = list(map(int, input().split()))

root = None
for v in values:
    root = insert(root, v)

print(count_triangles(root))
#G
#H
#I
#J
def build_order(sorted_arr):
    n = len(sorted_arr)
    if n == 0:
        return []
    mid = n // 2
    return [sorted_arr[mid]] + build_order(sorted_arr[:mid]) + build_order(sorted_arr[mid+1:])

def main():
    k = int(input().strip())
    n = (1 << k) - 1  # 2^k - 1
    arr = list(map(int, input().split()))
    arr.sort()
    order = build_order(arr)
    print(' '.join(map(str, order)))

if __name__ == "__main__":
    main()
#A
n = int(input())                
arr = list(map(int, input().split()))  
x = int(input())               
min_dist = abs(arr[0] - x)  
index = 0                 
for i in range(1, n):
    dist = abs(arr[i] - x)  
    if dist < min_dist:     
        min_dist = dist
        index = i          
print(index)

#B
n, k = map(int, input().split())
words = input().split()
k = k % n  
shifted = words[k:] + words[:k]
print(" ".join(shifted))

#C
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_every_second(self):
        current = self.head
        while current and current.next:
            current.next = current.next.next
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next

n = int(input())
values = list(map(int, input().split()))
ll = LinkedList()
for val in values:
    ll.append(val)
ll.delete_every_second()
ll.print_list()

#D
n = int(input())
arr = list(map(int, input().split()))
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_count = max(freq.values())
modes = [num for num, c in freq.items() if c == max_count]
modes.sort(reverse=True)
print(" ".join(map(str, modes)))

#E
n = int(input())
names = [input().strip() for _ in range(n)]
unique_names = []
for i in range(n):
    if i == 0 or names[i] != names[i - 1]:
        unique_names.append(names[i])
print(f"All in all: {len(unique_names)}")
print("Students:")
for name in reversed(unique_names):
    print(name)


#F
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if current:
            new_node.next = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
n = int(input())
ll = LinkedList()
for _ in range(n):
    val = int(input())
    ll.append(val)
data = int(input())     
position = int(input()) 
ll.insert_at_position(data, position)
ll.print_list()

#H
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def insert(head, x, p):
    new_node = Node(x)
    if p == 0:  
        new_node.next = head
        return new_node
    cur = head
    for _ in range(p - 1):
        cur = cur.next
    new_node.next = cur.next
    cur.next = new_node
    return head
def remove(head, p):
    if p == 0:
        return head.next
    cur = head
    for _ in range(p - 1):
        cur = cur.next
    cur.next = cur.next.next
    return head

def print_list(head):
    if not head:
        print(-1)
        return
    res = []
    cur = head
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print(" ".join(res))

def replace(head, p1, p2):
    if p1 == p2:
        return head

    dummy = Node(0)
    dummy.next = head
    prev1 = dummy
    for _ in range(p1):
        prev1 = prev1.next
    node = prev1.next
    prev1.next = node.next

    prev2 = dummy
    for _ in range(p2):
        prev2 = prev2.next
    node.next = prev2.next
    prev2.next = node
    return dummy.next
def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def cyclic_left(head, x):
    if not head or not head.next:
        return head

    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    x %= length
    if x == 0:
        return head

    cur = head
    for _ in range(x - 1):
        cur = cur.next
    new_head = cur.next
    cur.next = None

    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = head
    return new_head

def cyclic_right(head, x):
    if not head or not head.next:
        return head
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    x %= length
    if x == 0:
        return head
    return cyclic_left(head, length - x)

def main():
    import sys
    head = None
    for line in sys.stdin:
        parts = list(map(int, line.split()))
        if not parts:
            continue
        cmd = parts[0]
        if cmd == 0:
            break
        elif cmd == 1:
            x, p = parts[1], parts[2]
            head = insert(head, x, p)
        elif cmd == 2:
            p = parts[1]
            head = remove(head, p)
        elif cmd == 3:
            print_list(head)
        elif cmd == 4:
            p1, p2 = parts[1], parts[2]
            head = replace(head, p1, p2)
        elif cmd == 5:
            head = reverse(head)
        elif cmd == 6:
            x = parts[1]
            head = cyclic_left(head, x)
        elif cmd == 7:
            x = parts[1]
            head = cyclic_right(head, x)
if __name__ == "__main__":
    main()

#I
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_front(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print("ok")

    def add_back(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print("ok")

    def erase_front(self):
        if not self.head:
            print("error")
            return
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        print(val)

    def erase_back(self):
        if not self.tail:
            print("error")
            return
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        print(val)

    def front(self):
        if not self.head:
            print("error")
        else:
            print(self.head.val)

    def back(self):
        if not self.tail:
            print("error")
        else:
            print(self.tail.val)

    def clear(self):
        self.head = None
        self.tail = None
        print("ok")

def main():
    import sys
    dll = DoublyLinkedList()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        cmd = parts[0]

        if cmd == "add_front":
            dll.add_front(parts[1])
        elif cmd == "add_back":
            dll.add_back(parts[1])
        elif cmd == "erase_front":
            dll.erase_front()
        elif cmd == "erase_back":
            dll.erase_back()
        elif cmd == "front":
            dll.front()
        elif cmd == "back":
            dll.back()
        elif cmd == "clear":
            dll.clear()
        elif cmd == "exit":
            print("goodbye")
            break

if __name__ == "__main__":
    main()

#K
from collections import deque
T = int(input())
for _ in range(T):
    N = int(input())
    chars = input().split()
    freq = {}
    q = deque()
    result = []
    for ch in chars:
        freq[ch] = freq.get(ch, 0) + 1
        if freq[ch] == 1:
            q.append(ch)
        while q and freq[q[0]] > 1:
            q.popleft()
        if q:
            result.append(q[0])
        else:
            result.append('-1')
    print(' '.join(result) + ' ')

#L
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def findMaxSum(n: int, head: ListNode) -> int:
    current = head
    max_sum = current.val
    current_sum = 0
    while current:
        current_sum += current.val
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
        current = current.next
    return max_sum
n = int(input())
a = list(map(int, input().split()))
head = ListNode(a[0])
tail = head
for i in range(1, n):
    tmp = ListNode(a[i])
    tail.next = tmp
    tail = tmp
print(findMaxSum(n, head))
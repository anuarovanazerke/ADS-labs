#A
from collections import deque
def build_deck(n: int):
    dq = deque()
    for i in range(n, 0, -1):
        dq.appendleft(i)      
        dq.rotate(i)          
    return dq
def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        deck = build_deck(n)
        results.append(" ".join(map(str, deck)))
    print("\n".join(results))
if __name__ == "__main__":
    main()

#B
def nearest_not_greater(arr):
    stack = []
    res = []
    for x in arr:
        while stack and stack[-1] > x:
            stack.pop()
        if stack:
            res.append(stack[-1])
        else:
            res.append(-1)
        stack.append(x)
    return res
def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    ans = nearest_not_greater(arr)
    print(" ".join(map(str, ans)))
if __name__ == "__main__":
    main()

#C
def process(s: str) -> str:
    stack = []
    for ch in s:
        if ch == "#":
            if stack:
                stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)
s1, s2 = input().split()
if process(s1) == process(s2):
    print("Yes")
else:
    print("No")


#D
def is_balanced(s: str) -> bool:
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()   
        else:
            stack.append(ch)
    return not stack

s = input().strip()
print("YES" if is_balanced(s) else "NO")

#E
from collections import deque
def play_game(boris_cards, nursik_cards):
    boris = deque(boris_cards)
    nursik = deque(nursik_cards)
    moves = 0
    MAX_MOVES = 10**6
    while boris and nursik and moves < MAX_MOVES:
        moves += 1
        b = boris.popleft()
        n = nursik.popleft()
        if (b == 0 and n == 9) or (b > n and not (b == 9 and n == 0)):
            boris.append(b)
            boris.append(n)
        else:
            nursik.append(b)
            nursik.append(n)
    if moves >= MAX_MOVES:
        print("Draw")
    elif not boris:
        print("Nursik", moves)
    else:
        print("Boris", moves)
boris_cards = list(map(int, input().split()))
nursik_cards = list(map(int, input().split()))
play_game(boris_cards, nursik_cards)

#F
import math
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
n = int(input())
count = 0
num = 1
while count < n:
    num += 1
    if is_prime(num):
        count += 1
print(num)

#G
import math
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
n = int(input())
primes = []
superprimes = []
num = 2
while len(superprimes) < n:
    if is_prime(num):
        primes.append(num)
      
        if is_prime(len(primes)):
            superprimes.append(num)
    num += 1
print(superprimes[-1])

#H
import math
n = int(input())
if n < 2:
    print("NO")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("YES" if is_prime else "NO")

#I
from collections import deque
import sys
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
s_queue = deque()
k_queue = deque()
for i, ch in enumerate(s):
    if ch == 'S':
        s_queue.append(i)
    else:
        k_queue.append(i)
while s_queue and k_queue:
    si = s_queue.popleft()
    ki = k_queue.popleft()
    if si < ki:
        s_queue.append(si + n)
    else:
        k_queue.append(ki + n)
print("SAKAYANAGI" if s_queue else "KATSURAGI")

#J
from collections import deque
import sys
dq = deque()
out = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if line == "!":
        break
    if line[0] == '+':
        _, x = line.split()
        dq.appendleft(int(x))
    elif line[0] == '-':
        _, x = line.split()
        dq.append(int(x))
    elif line[0] == '*':
        if not dq:
            out.append("error")
        elif len(dq) == 1:
            val = dq.popleft()
            out.append(str(val * 2))
        else:
            first = dq.popleft()
            last = dq.pop()
            out.append(str(first + last))
print("\n".join(out))
#A
import heapq
def min_merge_cost(arr):
    heapq.heapify(arr)  
    total_cost = 0
    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        cost = first + second
        total_cost += cost
        heapq.heappush(arr, cost)
    return total_cost

n = int(input())
sizes = list(map(int, input().split()))
print(min_merge_cost(sizes))

#B
import heapq
def rock_game(stones):
    stones = [-x for x in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = -heapq.heappop(stones)
        second = -heapq.heappop(stones)

        if first != second:
            heapq.heappush(stones, -(first - second))
    return -stones[0] if stones else 0

n = int(input())
stones = list(map(int, input().split()))

print(rock_game(stones))

#C
import heapq
n, m = map(int, input().split())
rows = list(map(int, input().split()))
heap = [-x for x in rows]
heapq.heapify(heap)
total = 0
for _ in range(m):
    x = -heapq.heappop(heap)
    total += x
    if x > 1:
        heapq.heappush(heap, -(x - 1))
print(total)

#D
import heapq
n, k = map(int, input().split())
mixtures = list(map(int, input().split()))
heapq.heapify(mixtures)
count = 0
while mixtures and mixtures[0] < k:
    if len(mixtures) < 2:
        print(-1)
        break
    a = heapq.heappop(mixtures)
    b = heapq.heappop(mixtures)
    new = a + 2 * b  
    heapq.heappush(mixtures, new)
    count += 1
else:
    print(count)

#E
import heapq
n, k = map(int, input().split())
heap = []  
total = 0 
for _ in range(n):
    command = input().split()

    if command[0] == "insert":
        x = int(command[1])
        if len(heap) < k:
            heapq.heappush(heap, x)
            total += x
        else:
            if x > heap[0]:
                total += x - heap[0]
                heapq.heapreplace(heap, x)
      
    elif command[0] == "print":
        print(total)

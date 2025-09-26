#A
t = int(input())
queries = list(map(int, input().split()))
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
pos = dict()
for i in range(n):
    for j in range(m):
        pos[matrix[i][j]] = (i, j)
for q in queries:
    if q in pos:
        print(pos[q][0], pos[q][1])
    else:
        print(-1)

#B
def can_divide(arr, k, max_sum):
    current_sum = 0
    count = 1 
    for num in arr:
        if num > max_sum:
            return False  
        if current_sum + num <= max_sum:
            current_sum += num
        else:
            count += 1
            current_sum = num
            if count > k:
                return False
    return True
def min_max_sum(arr, k):
    left = max(arr)  
    right = sum(arr) 
    while left < right:
        mid = (left + right) // 2
        if can_divide(arr, k, mid):
            right = mid
        else:
            left = mid + 1
    return left
n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(min_max_sum(arr, k))

#C
import bisect
def count_leq(a, x):
    return bisect.bisect_right(a, x)
def count_range(a, l, r):
    if l > r:
        return 0
    return count_leq(a, r) - count_leq(a, l - 1)
def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    n, q = map(int, input_data[:2])
    arr = list(map(int, input_data[2:2+n]))
    queries = input_data[2+n:]
    
    arr.sort()
    
    for i in range(q):
        l1, r1, l2, r2 = map(int, queries[4*i:4*i+4])
        c1 = count_range(arr, l1, r1)
        c2 = count_range(arr, l2, r2)
        L = max(l1, l2)
        R = min(r1, r2)
        c_inter = count_range(arr, L, R)
        
        ans = c1 + c2 - c_inter
        print(ans)

if __name__ == "__main__":
    main()

#D
import bisect
def count_leq(a, x):
    return bisect.bisect_right(a, x)
def count_range(a, l, r):
    if l > r:
        return 0
    return count_leq(a, r) - count_leq(a, l-1)
def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    n, q = map(int, input_data[:2])
    arr = list(map(int, input_data[2:2+n]))
    queries = input_data[2+n:]
    arr.sort()
    for i in range(q):
        l1, r1, l2, r2 = map(int, queries[4*i:4*i+4])
        c1 = count_range(arr, l1, r1)
        c2 = count_range(arr, l2, r2)
        L, R = max(l1, l2), min(r1, r2)
        c_inter = count_range(arr, L, R)
        print(c1 + c2 - c_inter)
if __name__ == "__main__":
    main()

#E
def can_catch(sheep_list, L, k):
    count = 0
    for (x1, y1, x2, y2) in sheep_list:
        if x1 >= 0 and y1 >= 0 and x2 <= L and y2 <= L:
            count += 1
            if count >= k:
                return True
    return False
def find_min_length(n, k, sheep_list):
    max_coord = 0
    for x1, y1, x2, y2 in sheep_list:
        max_coord = max(max_coord, x1, y1, x2, y2)

    low, high = 0, max_coord

    while low < high:
        mid = (low + high) // 2
        if can_catch(sheep_list, mid, k):
            high = mid
        else:
            low = mid + 1

    return low
n, k = map(int, input().split())
sheep_list = [tuple(map(int, input().split())) for _ in range(n)]
print(find_min_length(n, k, sheep_list))

#F
import bisect
N = int(input())
powers = list(map(int, input().split()))
Q = int(input())
powers.sort()
prefix = [0] * N
prefix[0] = powers[0]
for i in range(1, N):
    prefix[i] = prefix[i-1] + powers[i]
for _ in range(Q):
    p = int(input())
    idx = bisect.bisect_right(powers, p)
    count = idx
    total_power = prefix[idx-1] if idx > 0 else 0
    print(count, total_power)

#G
def can_deliver(a, k, capacity):
    flights = 0
    for gifts in a:
        flights += (gifts + capacity - 1) // capacity
    return flights <= k
n, k = map(int, input().split())
a = list(map(int, input().split()))
left = 1
right = max(a) 
right = sum(a)
while left < right:
    mid = (left + right) // 2
    if can_deliver(a, k, mid):
        right = mid
    else:
        left = mid + 1
print(left)

#H
import bisect
def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    blocks = data[2:2+n]
    mistakes = data[2+n:]
    end = []
    total = 0
    for b in blocks:
        total += b
        end.append(total)
    for x in mistakes:
        block = bisect.bisect_left(end, x) + 1
        print(block)
if __name__ == "__main__":
    main()

#I
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
if binary_search(arr, x):
    print("Yes")
else:
    print("No")

#J
def can_steal_all(bags, speed, h):
    hours = 0
    for bars in bags:
        hours += (bars + speed - 1) // speed 
    return hours <= h
def min_stealing_speed(bags, h):
    left, right = 1, max(bags) 
    result = right

    while left <= right:
        mid = (left + right) // 2
        if can_steal_all(bags, mid, h):
            result = mid
            right = mid - 1 
        else:
            left = mid + 1 
    return result
def main():
    n, h = map(int, input().split())
    bags = list(map(int, input().split()))
    print(min_stealing_speed(bags, h))
if __name__ == "__main__":
    main()

#K
def min_subarray_length(arr, k):
    n = len(arr)
    left = 0
    current_sum = 0
    min_len = n + 1 
    for right in range(n):
        current_sum += arr[right]
        while current_sum >= k:
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1
    return min_len
def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_subarray_length(arr, k))
if __name__ == "__main__":
    main()


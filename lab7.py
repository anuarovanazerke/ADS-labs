#A
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if len(left[i]) <= len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
n = int(input()) 
for _ in range(n):
    words = input().split()
    sorted_words = merge_sort(words)
    print(' '.join(sorted_words))

#B
def merge_arrays(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
merged = merge_arrays(A, B)
print(*merged)

#C
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def find_common(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return result
n, m = map(int, input().split())
A = list(map(int, input().split())) if n > 0 else []
B = list(map(int, input().split())) if m > 0 else []
A_sorted = merge_sort(A)
B_sorted = merge_sort(B)
common = find_common(A_sorted, B_sorted)
if common:
    print(*common)
else:
    print()

#D
gpa_scale = {
    'A+': 4.00, 'A': 3.75, 'B+': 3.50, 'B': 3.00,
    'C+': 2.50, 'C': 2.00, 'D+': 1.50, 'D': 1.00, 'F': 0.00
}
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][2] < right[j][2]:
            result.append(left[i])
            i += 1
        elif left[i][2] > right[j][2]:
            result.append(right[j])
            j += 1
        else:
            if left[i][0] < right[j][0]:
                result.append(left[i])
                i += 1
            elif left[i][0] > right[j][0]:
                result.append(right[j])
                j += 1
            else: 
                if left[i][1] <= right[j][1]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

n = int(input())
students = []
for _ in range(n):
    parts = input().split()
    lastname = parts[0]
    firstname = parts[1]
    subj_count = int(parts[2])
    total_points = 0.0
    total_credits = 0
    idx = 3
    for _ in range(subj_count):
        mark = parts[idx]
        credits = int(parts[idx + 1])
        total_points += gpa_scale[mark] * credits
        total_credits += credits
        idx += 2
    gpa = total_points / total_credits if total_credits > 0 else 0.0
    students.append((lastname, firstname, gpa))
sorted_students = merge_sort(students)
for last, first, gpa in sorted_students:
    print(f"{last} {first} {gpa:.3f}")

#E
def merge(left, right):
    res, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        a, b = left[i], right[j]
        sum_a, sum_b = sum(a), sum(b)
        if sum_a > sum_b:
            res.append(a); i += 1
        elif sum_a < sum_b:
            res.append(b); j += 1
        else:
            if a <= b:
                res.append(a); i += 1
            else:
                res.append(b); j += 1
    res.extend(left[i:]); res.extend(right[j:])
    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

n, m = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(n)]
sorted_rows = merge_sort(rows)
for row in sorted_rows:
    print(*row, end=' \n')

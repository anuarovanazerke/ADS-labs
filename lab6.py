#A
n = int(input())      
s = input().strip()   
vowels = set("aeiou")
vowel_letters = sorted([ch for ch in s if ch in vowels])
consonant_letters = sorted([ch for ch in s if ch not in vowels])
result = ''.join(vowel_letters + consonant_letters)
print(result)

#B
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
try:
    n, m = map(int, input().split())
except:
    exit()
a = list(map(int, input().split())) if n > 0 else []
b = list(map(int, input().split())) if m > 0 else []
if not a or not b:
    exit()
a = merge_sort(a)
b = merge_sort(b)
i = j = 0
common = []
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        common.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
if common:
    print(' '.join(map(str, common)) + ' ')

#C
n = int(input())
points = list(map(int, input().split()))
points.sort()
min_diff = float('inf')
for i in range(n - 1):
    diff = abs(points[i + 1] - points[i])
    if diff < min_diff:
        min_diff = diff
result = []
for i in range(n - 1):
    if abs(points[i + 1] - points[i]) == min_diff:
        result.extend([points[i], points[i + 1]])

print(*result)

#D
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    d_p, m_p, y_p = map(int, pivot.split('-'))
    left = []
    middle = []
    right = []
    for date in arr:
        d, m, y = map(int, date.split('-'))
        if (y, m, d) < (y_p, m_p, d_p):
            left.append(date)
        elif (y, m, d) > (y_p, m_p, d_p):
            right.append(date)
        else:
            middle.append(date)
    return quick_sort(left) + middle + quick_sort(right)
n = int(input())
dates = [input().strip() for _ in range(n)]
sorted_dates = quick_sort(dates)
for d in sorted_dates:
    print(d)

#E
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for col in range(m):
    column = [matrix[row][col] for row in range(n)]
    sorted_column = bubble_sort_desc(column)
    for row in range(n):
        matrix[row][col] = sorted_column[row]

for row in matrix:
    print(' '.join(map(str, row)) + ' ')

#F
grade_to_gpa = {
    "A+": 4.00, "A": 3.75, "B+": 3.50, "B": 3.00,
    "C+": 2.50, "C": 2.00, "D+": 1.50, "D": 1.00, "F": 0.00
}
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        last_l, first_l, gpa_l = left[i]
        last_r, first_r, gpa_r = right[j]
        if gpa_l < gpa_r:
            res.append(left[i]); i += 1
        elif gpa_l > gpa_r:
            res.append(right[j]); j += 1
        else:
            if last_l < last_r:
                res.append(left[i]); i += 1
            elif last_l > last_r:
                res.append(right[j]); j += 1
            else:
                if first_l <= first_r:
                    res.append(left[i]); i += 1
                else:
                    res.append(right[j]); j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
it = iter(data)
n = int(next(it))
students = []
for _ in range(n):
    last = next(it)
    first = next(it)
    k = int(next(it))
    total_points = 0.0
    total_credits = 0
    for _s in range(k):
        mark = next(it)
        credit = int(next(it))
        total_points += grade_to_gpa[mark] * credit
        total_credits += credit
    gpa = total_points / total_credits if total_credits > 0 else 0.0
    students.append((last, first, gpa))

students = merge_sort(students)
for last, first, gpa in students:
    print(f"{last} {first} {gpa:.3f}")

#G
def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

n = int(input())
old_to_new = {}
new_to_old = {}

for _ in range(n):
    old, new = input().split()
    if old in new_to_old:
        original = new_to_old[old]
        old_to_new[original] = new
        new_to_old[new] = original
        del new_to_old[old]
    else:
        old_to_new[old] = new
        new_to_old[new] = old
result = list(old_to_new.items())
sorted_result = merge_sort(result)
print(len(sorted_result))
for old, new in sorted_result:
    print(old, new)

#H
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

n = int(input())
letters = input().split()
target = input().strip()
letters = quick_sort(letters)
balanced = None
for ch in letters:
    if ch > target:
        balanced = ch
        break
if balanced is None:
    balanced = letters[0]
print(balanced)

#I
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
s = input().strip()
letters = list(s)
sorted_letters = quick_sort(letters)
print(''.join(sorted_letters))
#A
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0 
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0 

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return True 
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

def min_repetitions(A, B):
    repeated = A
    count = 1

    while len(repeated) < len(B):
        repeated += A
        count += 1

    for _ in range(2):
        if kmp_search(repeated, B):
            return count
        repeated += A
        count += 1

    return -1

A = input().strip()
B = input().strip()
print(min_repetitions(A, B))

#B
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def count_occurrences(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0
    count = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                count += 1
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count

data = input().split()
password = data[0]
k = int(data[1])
text = input().strip()

occ = count_occurrences(text, password)
print("YES" if occ >= k else "NO")

#C
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0
    positions = []
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                positions.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return positions


def cyclic_shift(s, t):
    if len(s) != len(t):
        return -1

    doubled = s + s
    positions = kmp_search(doubled, t)

    n = len(s)
    for pos in positions:
        if pos < n: 
            return (n - pos) % n
    return -1

s = input().strip()
t = input().strip()
print(cyclic_shift(s, t))

#D
def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def matching_suffix_prefix(prev_low, city_low):
    combined = city_low + '#' + prev_low
    pi = prefix_function(combined)
    return pi[-1]

def main():
    prev = input().strip()
    if not prev:
        print(0)
        return

    n = int(input().strip())
    cities = [input().strip() for _ in range(n)]

    prev_low = prev.lower()

    max_len = 0
    results = []

    for city in cities:
        city_low = city.lower()
        L = matching_suffix_prefix(prev_low, city_low)
        if L > max_len:
            max_len = L
            results = [city]
        elif L == max_len:
            results.append(city)

    if max_len == 0:
        print(0)
    else:
        print(len(results))
        for name in results:
            print(name)

if __name__ == "__main__":
    main()


#E
def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def main():
    t = int(input().strip())
    for _ in range(t):
        s, k = input().split()
        k = int(k)
        pi = prefix_function(s)
        overlap = pi[-1]  
        result = len(s) + (k - 1) * (len(s) - overlap)
        print(result)

if __name__ == "__main__":
    main()

#F
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0
    indices = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                indices.append(i - j + 1)  
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return indices


text = input().strip()
pattern = input().strip()
indices = kmp_search(text, pattern)
print(len(indices))
if indices:
    print(*indices)

#G
def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def main():
    s = input().strip()
    pi = prefix_function(s)
    n = len(s)
    answer = n - pi[-1]
    print(answer)

if __name__ == "__main__":
    main()

#H
#include <bits/stdc++.h>
using namespace std;

vector<int> z_function(const string &s) {
    int n = (int)s.size();
    vector<int> z(n);
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i <= r)
            z[i] = min(r - i + 1, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            z[i]++;
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    int n = s.size();

    vector<int> z = z_function(s);
    long long cnt = 0;

    for (int L = 1; 2 * L < n; L++) {
        if (z[L] >= L)
            cnt++;
    }

    cout << cnt << "\n";
    return 0;
}

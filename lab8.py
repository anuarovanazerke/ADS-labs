#H
def rabin_karp_hashes(s, L, base=257, mod=10**9 + 7):
    if L > len(s):
        return set()

    h = 0
    power = pow(base, L - 1, mod)
    hashes = set()
    for i in range(L):
        h = (h * base + ord(s[i])) % mod
    hashes.add(h)

    for i in range(L, len(s)):
        h = (h - ord(s[i - L]) * power) % mod
        h = (h * base + ord(s[i])) % mod
        hashes.add(h)

    return hashes


def longest_common_substring(strings):
    left, right = 0, min(len(s) for s in strings)
    best_sub = ""

    while left <= right:
        mid = (left + right) // 2
        common_hashes = rabin_karp_hashes(strings[0], mid)

        for s in strings[1:]:
            common_hashes &= rabin_karp_hashes(s, mid)
            if not common_hashes:
                break

        if common_hashes:
            left = mid + 1
            substrs = set()
            base, mod = 257, 10**9 + 7
            h = 0
            power = pow(base, mid - 1, mod)
            for i in range(mid):
                h = (h * base + ord(strings[0][i])) % mod
            if h in common_hashes:
                best_sub = strings[0][:mid]
            for i in range(mid, len(strings[0])):
                h = (h - ord(strings[0][i - mid]) * power) % mod
                h = (h * base + ord(strings[0][i])) % mod
                if h in common_hashes:
                    best_sub = strings[0][i - mid + 1:i + 1]
        else:
            right = mid - 1

    return best_sub

K = int(input())
strings = [input().strip() for _ in range(K)]

print(longest_common_substring(strings))


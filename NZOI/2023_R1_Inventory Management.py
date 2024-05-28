n, k = map(int, input().split())
d = list(map(int, input().split()))
d.sort(reverse=True)

if k >= n:
    maxi = sum(d)
else:
    maxi = sum(d[:k])

print(maxi)

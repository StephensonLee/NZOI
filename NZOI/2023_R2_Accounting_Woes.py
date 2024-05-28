n = int(input())
costs = list(map(int, input().split()))
print((n - sum(costs) % n) % n)

from bisect import bisect_left

n = int(input())
bids = []
for i in range(n):
    bids.append(int(input()))

m = int(input())
prices = []
for i in range(m):
    prices.append(int(input()))

revenue = 0
bids.sort()
prices.sort()

for bid in bids:
    if len(prices) == 0:
        break
    ind = bisect_left(prices, bid)
    if ind == len(prices):
        revenue += prices[-1]
        del (prices[-1])
    elif bid == prices[ind]:
        revenue += prices[ind]
        del (prices[ind])
    elif ind > 0:
        revenue += prices[ind - 1]
        del (prices[ind - 1])

print(revenue)

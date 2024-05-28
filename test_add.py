prices = [7, 1, 5, 3, 6, 4]


def maxProfit(prices):
    lower = prices[0]
    profits = []

    for i in range(1, len(prices)):
        profit = prices[i] - lower
        profits.append(profit)
        if prices[i] < lower:
            lower = prices[i]

            print(lower)

    return max(profits)


print(maxProfit(prices))

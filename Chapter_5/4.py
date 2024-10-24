def knapsack(items, weight_limit):
    n = len(items)
    dp = [0] * (weight_limit + 1)

    for weight, value in items:
        for w in range(weight_limit, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[weight_limit]

items_1 = [(2, 10), (3, 15), (5, 30)]
weight_limit_1 = 5

max_profit_1 = knapsack(items_1, weight_limit_1)

max_profit_1

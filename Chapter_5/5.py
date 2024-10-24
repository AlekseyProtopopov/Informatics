def knapsack_multi_constraints(items, time_limit, weight_limit):
    n = len(items)
    dp = [[[0] * (weight_limit + 1) for _ in range(time_limit + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, time, weight = items[i - 1]
        for t in range(time_limit + 1):
            for w in range(weight_limit + 1):
                dp[i][t][w] = dp[i - 1][t][w]
                if t >= time and w >= weight:
                    dp[i][t][w] = max(dp[i][t][w], dp[i - 1][t - time][w - weight] + value)

    return dp[n][time_limit][weight_limit]

items_1 = [(10, 5, 2), (15, 4, 3), (30, 7, 5)]
time_limit_1 = 10
weight_limit_1 = 10

max_profit_1 = knapsack_multi_constraints(items_1, time_limit_1, weight_limit_1)

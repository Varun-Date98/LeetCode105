from typing import List


'''
122. Best Time to Buy and Sell Stock II | Medium
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of
the stock at any time. However, you can buy it then immediately sell it on the same day.Find and
return the maximum profit you can achieve.
---------------------------------------------------------------------------------------------------

'''


def maxProfit(prices: List[int]) -> int:
    cost = prices[0]
    dp = [0] * (len(prices) + 1)

    for i in range(1, len(prices) + 1):
        if cost < prices[i - 1]:
            dp[i] = dp[i - 1] + (prices[i - 1] - cost)
        else:
            dp[i] = dp[i - 1]
        
        cost = prices[i - 1]

    return dp[-1]

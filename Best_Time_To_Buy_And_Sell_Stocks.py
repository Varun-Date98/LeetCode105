from typing import List


'''
121. Best Time to Buy and Sell Stock | Easy
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock. Return the maximum profit you can achieve
from this transaction. If you cannot achieve any profit, return 0.
-------------------------------------------------------------------------------------------

'''


def maxProfit(prices: List[int]) -> int:
    res = 0
    bestBuy = prices[0]

    for i in range(1, len(prices)):
        res = max(res, prices[i] - bestBuy)
        bestBuy = min(bestBuy, prices[i])
    
    return res

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf')
        max_profit = 0
    
        for cur_price in prices:
            buy_price = min(buy_price, cur_price)
            
            profit = cur_price - buy_price
            
            max_profit = max(max_profit, profit)

        return max_profit


if __name__ == "__main__":
    prices_1 = [7,1,5,3,6,4]
    prices_2 = [7,6,4,3,1]

    s = Solution()
    o = s.maxProfit(prices_1)
    print(o)
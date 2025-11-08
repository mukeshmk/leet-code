from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}

        for a in range(1, amount + 1):
            minn = float("inf")
            for c in coins:
                sub_prob = a - c
                if sub_prob >= 0 and sub_prob in memo:
                    minn = min(minn, memo[sub_prob] + 1)
            if minn != float('inf'):
                memo[a] = minn
        
        return memo.get(amount, -1)



if __name__ == "__main__":
    coins_1 = [1,2,5]
    amount_1 = 21
    coins_2 = [2]
    amount_2 = 3
    coins_3 = [1]
    amount_3 = 0

    s = Solution()
    o = s.coinChange(coins_2, amount_2)
    print(o)

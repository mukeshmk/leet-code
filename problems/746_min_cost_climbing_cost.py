class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        
        dp = [0] * (n + 1)
        
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, n + 1):
            one_step = dp[i - 1] + cost[i - 1]
            two_steps = dp[i - 2] + cost[i - 2]
            dp[i] = min(one_step, two_steps)
        
        return dp[n]

if __name__ == "__main__":
    cost_1 = [10,15,20]
    cost_2 = [1,100,1,1,1,100,1,1,100,1]

    s = Solution()
    o = s.lengthOfLastWord(cost_2)
    print(o)


class Solution:
    def divisorGame(self, n):
        dp = [False] * (n + 1)
        dp[0] = False 
        dp[1] = False
        for i in range(2, n + 1):
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break
        return dp[n]
        
if __name__ == "__main__":
    n_1 = 2
    n_2 = 3

    s = Solution()
    o = s.divisorGame(n_2)
    print(o)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        memo[0] = 0
        memo[1] = 1
        memo[2] = 2

        for i in range(3, n + 1):
            memo[i] = 0
            for step in [1, 2]:
                subprob = i - step
                if subprob < 0:
                    continue
                memo[i] = memo[i] + memo[subprob]
        
        return memo[n]
        
if __name__ == "__main__":
    n_1 = 2
    n_2 = 3

    s = Solution()
    o = s.climbStairs(n_2)
    print(o)


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
    
        dp = {}
        dp[0] = 0
        dp[1] = 1
        output = [0, 1]
        
        for i in range(2, n + 1):
            dp[i] = dp[i // 2] + (1 if i % 2 else 0)
            output.append(dp[i])
    
        return output

if __name__ == "__main__":
    n_1 = 2
    n_2 = 5

    s = Solution()
    o = s.countBits(n_2)
    print(o)
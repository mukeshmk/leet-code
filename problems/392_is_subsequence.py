class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) < len(s):
            return False
        elif len(t) == len(s):
            if s == t:
                return True
            else:
                return False
        else:
            dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
            for i in range(1, len(s) + 1):
                for j in range(1, len(t) + 1):
                    if s[i - 1] == t[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if dp[i][j] == len(s):
                return True
            else:
                return False

if __name__ == "__main__":
    s_1 = "abc"
    t_1 = "ahbgdc"
    s_2 = "axc"
    t_2 = "ahbgdc"

    s = Solution()
    o = s.isSubsequence(s_1, t_1)
    print(o)

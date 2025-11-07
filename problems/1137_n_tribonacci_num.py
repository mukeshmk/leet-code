class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            tn_0 = 0
            tn_1 = 1
            tn_2 = 1
            for _ in range(3, n + 1):
                tn_0, tn_1, tn_2 = tn_1, tn_2, tn_0 + tn_1 + tn_2
            return tn_2
        
if __name__ == "__main__":
    n_1 = 4
    n_2 = 5

    s = Solution()
    o = s.tribonacci(n_1)
    print(o)

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            prev, cur = 0, 1
            for _ in range(2, n + 1):
                prev, cur = cur, prev + cur
            return cur
        
if __name__ == "__main__":
    n_1 = 2
    n_2 = 3

    s = Solution()
    o = s.fib(n_2)
    print(o)

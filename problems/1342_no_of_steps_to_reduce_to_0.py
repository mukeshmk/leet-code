class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            steps += 1
        return steps

if __name__ == "__main__":
    n_1 = 14
    n_2 = 8
    n_3 = 123

    s = Solution()
    o = s.numberOfSteps(n_3)
    print(o)

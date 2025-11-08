from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0
        minn = float("inf")

        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                minn = min(minn, r - l + 1)
                summ -= nums[l]
                l += 1
        
        return minn if minn < float("inf") else 0



if __name__ == "__main__":
    target_1 = 7
    nums_1 = [2,3,1,2,4,3]
    target_2 = 4
    nums_2 = [1,4,4]
    target_3 = 11
    nums_3 = [1,1,1,1,1,1,1,1]
    target_4 = 7
    nums_1 = [2,3,1,2,4,3,1,2,1]
    target_5 = 11
    nums_5 = [1, 2, 3, 4, 5]


    s = Solution()
    o = s.minSubArrayLen(target_5, nums_5)
    print(o)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [float("-inf")] * len(nums)
        memo[0] = nums[0]

        for i in range(1, len(nums)):
            memo[i] = max(nums[i], memo[i - 1] + nums[i])
        
        return max(memo)


if __name__ == "__main__":
    nums_1 = [-2,1,-3,4,-1,2,1,-5,4]
    nums_2 = [1]
    nums_3 = [5,4,-1,7,8]

    s = Solution()
    o = s.maxSubArray(nums_1)
    print(o)

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor


if __name__ == "__main__":
    nums_1 = [2,2,1]
    nums_2 = [4,1,2,1,2]
    nums_3 = [1]

    s = Solution()
    o = s.singleNumber(nums_1)
    print(o)

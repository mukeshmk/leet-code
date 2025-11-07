from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

if __name__ == "__main__":
    nums_1 = [1,3,5,6]
    target_1 = 5
    nums_2 = [1,3,5,6]
    target_2 = 2
    nums_3 = [1,3,5,6]
    target_3 = 7

    s = Solution()
    o = s.searchInsert(nums_1, target_1)
    print(o)


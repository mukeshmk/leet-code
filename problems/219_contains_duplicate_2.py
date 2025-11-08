from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False

if __name__ == "__main__":
    nums_1 = [1,2,3,1]
    k_1 = 3
    nums_2 = [1,0,1,1]
    k_2 = 1
    nums_3 = [1,2,3,1,2,3]
    k_3 = 2
    nums_4 = [1,1,1,2,3,4]
    k_4 = 3

    s = Solution()
    o = s.containsNearbyDuplicate(nums_4, k_4)
    print(o)

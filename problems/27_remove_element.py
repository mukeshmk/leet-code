from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        return i

if __name__ == "__main__":
    nums_1 = [3,2,2,3]
    val_1 = 3
    nums_2 = [0,1,2,2,3,0,4,2]
    val_2 = 2

    s = Solution()
    o = s.removeElement(nums_2, val_2)
    print(o)


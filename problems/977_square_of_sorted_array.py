from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p = 0
        q = len(nums) - 1

        nums = [n ** 2 for n in nums]
        output = []

        while p <= q:
            if nums[p] > nums[q]:
                output.append(nums[p])
                p+=1
            else:
                output.append(nums[q])
                q-=1
        
        output.reverse()
        return output

if __name__ == "__main__":
    nums_1 = [-4,-1,0,3,10]
    nums_2 = [-7,-3,2,3,11]

    s = Solution()
    o = s.sortedSquares(nums_1)
    print(o)

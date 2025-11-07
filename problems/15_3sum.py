from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        for k in range(n - 2):
            
            if nums[k] > 0:
                break
            
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            i, j = k + 1, n - 1
            
            while i < j:
                summ = nums[k] + nums[i] + nums[j]
            
                if summ == 0:
                    output.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
            
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
            
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
            
                elif summ < 0:
                    i += 1
            
                else:
                    j -= 1
        
        return output

if __name__ == "__main__":
    nums_1 = [-1,0,1,2,-1,-4]
    nums_2 = [0,1,1]
    nums_3 = [0,0,0]

    s = Solution()
    o = s.threeSum(nums_1)
    print(o)

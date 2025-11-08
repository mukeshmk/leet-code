from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [nums[0]]
        for i in range(1, len(nums)):
            self.sums.append(self.sums[i - 1] + nums[i])
        
    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - (self.sums[left - 1] if left > 0 else 0)


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]

    s = NumArray(nums)
    o = s.sumRange(0, 2)
    print(o)
    o = s.sumRange(2, 5)
    print(o)
    o = s.sumRange(0, 5)
    print(o)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
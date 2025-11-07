
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1
        return [1] + digits

if __name__ == "__main__":
    digits_1 = [1,2,3]
    digits_2 = [4,3,2,1]

    s = Solution()
    o = s.plusOne(digits_2)
    print(o)


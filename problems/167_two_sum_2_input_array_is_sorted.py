class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        i = 0
        j = n - 1

        while i < j:
            summ = numbers[i] + numbers[j]
            if summ == target:
                return [i + 1, j + 1]
            elif summ > target:
                j -= 1
            else:
                i += 1

if __name__ == "__main__":
    numbers_1 = [2,7,11,15]
    target_1 = 9
    numbers_2 = [2,3,4]
    target_2 = 6
    numbers_3 = [-1,0]
    target_3 = -1

    s = Solution()
    o = s.twoSum(numbers_1, target_1)
    print(o)

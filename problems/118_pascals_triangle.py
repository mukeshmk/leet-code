from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        arr = []
        for i in range(numRows):
            sub_arr = []
            for j in range(i + 1):
                if j == 0:
                    sub_arr.append(1)
                elif i == j:
                    sub_arr.append(1)
                else:
                    sub_arr.append(arr[i - 1][j] + arr[i - 1][j - 1])
            arr.append(sub_arr)
        
        return arr
        
if __name__ == "__main__":
    numRows_1 = 5
    numRows_2 = 1

    s = Solution()
    o = s.generate(numRows_1)
    print(o)
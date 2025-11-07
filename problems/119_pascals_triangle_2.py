from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:

        arr = []
        for i in range(rowIndex + 1):
            sub_arr = []
            for j in range(i + 1):
                if j == 0:
                    sub_arr.append(1)
                elif i == j:
                    sub_arr.append(1)
                else:
                    sub_arr.append(arr[i - 1][j] + arr[i - 1][j - 1])
            arr.append(sub_arr)
        
        return arr[rowIndex]

if __name__ == '__main__':
    rowIndex_1 = 3
    rowIndex_2 = 0
    rowIndex_3 = 1

    s = Solution()
    o = s.getRow(rowIndex_1)
    print(o)

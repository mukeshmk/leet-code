from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []

        while matrix:
            # top R -> L
            output += (matrix.pop(0))

            # right U -> D
            if matrix and matrix[0]:
                for row in matrix:
                    output.append(row.pop())

            # down L -> R
            if matrix:
                output += (matrix.pop()[::-1])

            # left D -> U
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    output.append(row.pop(0))        
        return output


if __name__ == "__main__":
    matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    s = Solution()
    o = s.spiralOrder(matrix_2)
    print(o)

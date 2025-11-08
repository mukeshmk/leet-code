from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()

        output = []
        i = 0
        prev_min = float("inf")
        minn = float("inf")
        while i < n - 1:
            minn = min(minn, abs(arr[i] - arr[i + 1]) )
            if minn != prev_min:
                output = []
                prev_min = minn
            if abs(arr[i] - arr[i + 1]) == minn:
                output.append([arr[i], arr[i + 1]])
            i += 1
        return output



if __name__ == "__main__":
    arr_1 = [4,2,1,3]
    arr_2 = [1,3,6,10,15]
    arr_3 = [3,8,-10,23,19,-4,-14,27]

    s = Solution()
    o = s.minimumAbsDifference(arr_1)
    print(o)

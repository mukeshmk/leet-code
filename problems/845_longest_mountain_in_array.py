from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)

        peaks = []
        
        i = 1
        while i < n - 1:
            if arr[i-1] < arr[i] > arr[i + 1]:
                peaks.append(i)
            i += 1
        
        mountain = 0
        for peak in peaks:
            i = j = peak

            while i >= 0 and arr[i] > arr[i - 1]:
                i -= 1

            while j < n - 1 and arr[j] > arr[j + 1]:
                j += 1
    
            mountain = max(mountain, j - i + 1)

        return mountain


if __name__ == "__main__":
    arr_1 = [2,1,4,7,3,2,5]
    arr_2 = [2,2,2]
    arr_3 = [0,1,2,3,4,5,4,3,2,1,0]

    s = Solution()
    o = s.longestMountain(arr_3)
    print(o)

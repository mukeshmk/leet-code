class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)

        if ln > lh:
            return -1
        elif ln == lh:
            if haystack == needle:
                return 0
            else:
                return -1
        else:
            i = 0
            while i <= lh - ln:
                if needle == haystack[i:i+ln]:
                    return i
                i += 1
            return -1


if __name__ == '__main__':
    haystack_1 = "sadbutsad"
    needle_1 = "sad"
    haystack_2 = "leetcode"
    needle_2 = "leeto"

    s = Solution()
    o = s.strStr(haystack_1, needle_1)
    print(o)

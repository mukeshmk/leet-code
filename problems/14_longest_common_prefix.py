from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        
        strs = sorted(strs)
        
        first = strs[0]
        last = strs[-1]
        
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return common_prefix
            common_prefix+=first[i]
            
        return common_prefix

if __name__ == "__main__":
    strs_1 = ["flower","flow","flight"]
    strs_2 = ["dog","racecar","car"]

    s = Solution()
    o = s.longestCommonPrefix(strs_1)
    print(o)

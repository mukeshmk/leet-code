class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = [s.strip() for s in s.strip().split(" ")]
        return len(s[-1])
        
if __name__ == "__main__":
    s_1 = "Hello World"
    s_2 = "   fly me   to   the moon  "
    s_3 = "luffy is still joyboy"

    s = Solution()
    o = s.lengthOfLastWord(s_3)
    print(o)


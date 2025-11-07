class Solution:
    def isValid(self, input_str: str) -> bool:
        stack = []
        for ch in input_str:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if ch == ')' and top != '(':
                    return False
                if ch == ']' and top != '[':
                    return False
                if ch == '}' and top != '{':
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    s_1 = "()"
    s_2 = "()[]{}"
    s_3 = "(]"
    s_4 = "([])"
    s_5 = "([)]"

    s = Solution()
    o = s.isValid(s_5)
    print(o)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = "([{"
        closing_brackets = ")]}"
        bracket_map = {')': '(', ']': '[', '}': '{'}
        count_o, count_c = sum(b in opening_brackets for b in s), sum(b in closing_brackets for b in s)
        if count_o != count_c:
            return False
        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            elif bracket in closing_brackets:
                if not stack or stack[-1] != bracket_map[bracket]:
                    return False
                stack.pop()
        return True

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        length = 0
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(s[i])
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    length += 2
                else:
                    stack.append(s[i])
        return length


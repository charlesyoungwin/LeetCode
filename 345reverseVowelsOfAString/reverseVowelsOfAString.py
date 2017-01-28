import string
class Solution(object):
    def reverseVowels(self, s):
        """

        :type s: str
        :rtype: str
        """
        n = len(s)
        s1 = list(s)
        start = 0
        end = n - 1
        while start < end:
            while start < end and s1[start] != 'a' and s1[start] != 'e' and s1[start] != 'i' and s1[start] != 'o' and s1[start] != 'u' and s1[start] != 'A' and s1[start] != 'E' and s1[start] != 'I' and s1[start] != 'O' and s1[start] != 'U':
                start += 1
            while start < end and s1[end] != 'a' and s1[end] != 'e' and s1[end] != 'i' and s1[end] != 'o' and s1[end] != 'u' and s1[end] != 'A' and s1[end] != 'E' and s1[end] != 'I' and s1[end] != 'O' and s1[end] != 'U':
                end -= 1
            if start < end:
                tmp = s1[start]
                s1[start] = s1[end]
                s1[end] = tmp
            start += 1
            end -= 1
        s = ''.join(s1)
        return s

solu = Solution()
print(solu.reverseVowels('a.b,.'))

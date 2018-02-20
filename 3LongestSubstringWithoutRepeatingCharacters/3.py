class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        maxLength = 0
        start = 0
        for i in range(len(s)):
            if s[i] in dic:
                start = max(start, dic[s[i]] + 1)
            dic[s[i]] = i
            maxLength = max(maxLength, i - start + 1)
        return maxLength

if __name__ == '__main__':
    s = "abba"
    print(Solution().lengthOfLongestSubstring(s))
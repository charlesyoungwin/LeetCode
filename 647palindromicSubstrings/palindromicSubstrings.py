class Solution:
    def countSubstring(self, s):
        sLen = len(s)
        count = 0
        for i in range(sLen):
            for j in range(sLen):
                if self.isPalindromic(s, i, j) == True:
                    count += 1
        return count

    def isPalindromic(self, s, i, j):
        str = s[i:j+1]
        if str != '' and str == str[::-1]:
            return True
        else:
            return False


s = "aaa"
solu = Solution()
print(solu.countSubstring(s))


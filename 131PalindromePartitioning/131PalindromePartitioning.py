class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.backtrack(s, 0, [], res)
        return res

    def backtrack(self, s, index, temp, res):

        if index == len(s):
            res.append(list(temp))
        for i in range(index, len(s)):  
            if self.isPalindrome(s[index:i+1]):
                temp.append(s[index:i+1])
                self.backtrack(s, i + 1, temp, res)
                temp.pop()

    def isPalindrome(self, nums):
        return nums == nums[::-1]

if __name__ == '__main__':
    s = "aab"
    print(Solution().partition(s))
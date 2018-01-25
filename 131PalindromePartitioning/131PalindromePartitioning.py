class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        

    def backtrack(self, s, index, temp, res):

        if index == len(s):
            if all(temp, )

        for i in range(index, len(s)):  
            temp.append(s[i])
            self.backtrack(s, index + 1, temp, res)
            temp.pop(s[i])
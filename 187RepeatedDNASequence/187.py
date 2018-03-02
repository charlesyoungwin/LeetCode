class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        res = []
        for i in range(len(s) - 9):
            if s[i:i+10] in dic:
                if s[i:i+10] not in res:
                    res.append(s[i:i+10])
            else:
                dic[s[i:i+10]] = 1
        return res

if __name__ == '__main__':
    s = "AAAAAAAAAAAA"
    print(Solution().findRepeatedDnaSequences(s))


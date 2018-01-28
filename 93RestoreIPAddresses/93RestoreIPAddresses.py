class Solution:
    #accepted
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.backtrack(s, 0, res, "", 0)
        return res

    def backtrack(self, s, index, res, temp, count):
        if len(s) > 12 or count > 4:
            return
        if index == len(s) and count == 4:
            res.append(temp[:-1])
        for i in range(index, len(s)):
            if self.isIP(s[index:i + 1]):
                tmp = temp
                temp += s[index:i + 1] + "."
                self.backtrack(s, i + 1, res, temp, count + 1)
                temp = tmp

    def isIP(self, s):
        if len(s) > 1 and s[0] == '0':
            return False
        num = int(s)
        if num >= 0 and num <= 255:
            return True
        else:
            return False

if __name__ == '__main__':
    s = "25525511131"
    print(Solution().restoreIpAddresses(s))
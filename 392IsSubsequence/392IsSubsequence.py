class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        start = 0
        flag = 0
        for elem in s:
            ans = t.find(elem, start)
            if ans != -1:
                start = ans + 1
            else:
                flag = 1
                break
        if flag == 1:
            return False
        else:
            return True

    def isSubsequenceV2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t = iter(t)

        return all(c in t for c in s)

if __name__ == '__main__':
    s = "ac"
    t = "ahbgdc"
    print(Solution().isSubsequenceV2(s, t))
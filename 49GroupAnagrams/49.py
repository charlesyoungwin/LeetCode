class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        dic = {}
        for s in strs:
            sList = sorted(list(s))
            keyStr = "".join(sList)
            if keyStr not in dic:
                dic[keyStr] = []
            dic[keyStr].append(s)
        for key in dic:
            res.append(dic[key])
        return res

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
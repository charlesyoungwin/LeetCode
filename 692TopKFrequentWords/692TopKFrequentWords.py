class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = {}
        for item in words:
            dic[item] = dic.get(item, 0) + 1       
        ans = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
        res = []
        for i in range(k):
            res.append(ans[i][0])
        return res

if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    print(Solution().topKFrequent(words, 1))
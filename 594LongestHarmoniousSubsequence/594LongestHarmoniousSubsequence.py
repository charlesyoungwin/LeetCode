class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for item in nums:
            dic[item] = dic.get(item, 0) + 1
        res = 0
        for k in dic:
            v1 = dic.get(k - 1, 0) + dic[k]
            v2 = dic.get(k + 1, 0) + dic[k]
            if v1 != v2 and max(v1, v2) > res:
                res = max(v1, v2)
        return res

if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    print(Solution().findLHS(nums))

class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import collections
        nums.sort()
        res = []
        counter = collections.Counter(nums)
        for (k, v) in counter.items():
            if v == 2:
                res.append(k)
        for i in range(1, len(nums) + 1):
            if i not in counter:
                res.append(i)
        return res

if __name__ == '__main__':
    nums = [1, 2, 2, 4]
    print(Solution().findErrorNums(nums))

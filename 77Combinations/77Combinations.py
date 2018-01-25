class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, n+1)]
        res = []
        self.backtrack(nums, k, res, [], 0)
        return res
        
    def backtrack(self, nums, k, res, temp, start):
        if k == 0:
            res.append(list(temp))
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtrack(nums, k - 1, res, temp, i + 1)
            temp.pop()

if __name__ == '__main__':
    n = 4
    k = 2
    print(Solution().combine(n, k))
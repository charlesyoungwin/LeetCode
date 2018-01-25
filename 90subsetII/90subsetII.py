class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, [], res)
        new_res = []
        res = list(map(lambda x: sorted(x), res))
        for item in res:
            if item not in new_res:
                new_res.append(item)
        return new_res
    
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)


if __name__ == '__main__':
    nums = [4, 4, 4, 1, 4]
    print(Solution().subsetsWithDup(nums))
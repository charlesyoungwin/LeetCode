class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)
            

    def subsets2(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res

if __name__ == "__main__":
    solu = Solution()
    nums = [1, 2, 3, 4]
    print(solu.subsets(nums))

    print("solutino2:")
    print(solu.subsets2(nums))
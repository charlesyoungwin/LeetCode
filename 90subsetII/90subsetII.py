class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.backtrack(res, [], nums, 0)
        return res

    def backtrack(self, res, temp, nums, start):
        res.append(list(temp))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            self.backtrack(res, temp, nums, i + 1)
            temp.pop()


if __name__ == "__main__":
    solu = Solution()
    nums = [1, 2, 2]
    print(solu.subsetsWithDup(nums))


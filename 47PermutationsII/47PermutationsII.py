class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.backtrack(nums, res, [], [False] * len(nums))
        return res

    def backtrack(self, nums, res, temp, used):
        if len(temp) == len(nums):
            res.append(list(temp))
        else:
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                used[i] = True
                temp.append(nums[i])
                self.backtrack(nums, res, temp, used)
                used[i] = False
                temp.pop()

    def permuteUniqueV2(self, nums):
        res = []
        self.helper(nums, res, 0)
        return res

    def helper(self, nums, res, start):
        if start == len(nums):
            res.append(list(nums))
        for i in range(start, len(nums)):
            if(self.isUnique(nums, start, i)):
                temp = nums[start]
                nums[start] = nums[i]
                nums[i] = temp
                self.helper(nums, res, start + 1)
                temp = nums[start]
                nums[start] = nums[i]
                nums[i] = temp

    def isUnique(self, nums, start, end):
        for i in range(start, end):
            if nums[i] == nums[end]:
                return False
        return True

 
if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 2, 2, 3, 3]
    ans1 = solu.permuteUnique(nums)
    ans2 = solu.permuteUniqueV2(nums)
    for item in ans1:
        if item not in ans2:
            print("False")
    print("True")

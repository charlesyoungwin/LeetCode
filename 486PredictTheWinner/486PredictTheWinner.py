class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = {}
        return self.helper(nums, 0, len(nums) - 1, mem) >= 0

    def helper(self, nums, s, e, mem):
        # return nums[s] if s == e else max(nums[e] - self.helper(nums, s, e - 1),
        #                                   nums[s] - self.helper(nums, s + 1, e))
        if (s, e) not in mem:
            mem[(s, e)] = nums[s] if s == e else \
                max(nums[s] - self.helper(nums, s + 1, e, mem), nums[e] - self.helper(nums, s, e - 1, mem))
        return mem[(s, e)]

if __name__ == '__main__':
    nums = [1, 5, 233, 7]
    nums2 = [1, 5, 2]
    print(Solution().PredictTheWinner(nums))
    print(Solution().PredictTheWinner(nums2))

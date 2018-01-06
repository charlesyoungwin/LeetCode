class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def helper(nums, start, length = 0):

            if length == len(nums) - 1:
                res.append(list(nums))
            for i in range(start, len(nums)):
                if start == i:
                    helper(nums, start + 1, length + 1)
                if nums[start] != nums[i]:
                    nums[start], nums[i] = nums[i], nums[start]
                    helper(nums, start + 1, length + 1)
                    nums[start], nums[i] = nums[i], nums[start]

        helper(nums, 0)
        return res

if __name__ == '__main__':
    nums = [1, 2, 2]
    print(Solution().permute(nums))
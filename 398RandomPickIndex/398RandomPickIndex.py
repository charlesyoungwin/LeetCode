import random

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = []
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                res.append(i)
        return res[random.randint(0, len(res) - 1)]



# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 3, 3]
obj = Solution(nums)
print(obj.pick(3))
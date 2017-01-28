class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxConsecutiveOnes = 0
        count = 0
        i = -1
        while i < n:
            while i < n - 1 and nums[i + 1] == 1:
                i += 1
                count += 1
            i += 1
            if count > maxConsecutiveOnes:
                maxConsecutiveOnes = count
            count = 0
        return maxConsecutiveOnes

s = Solution()
nums = [1, 1, 0, 1, 1, 1]
print(s.findMaxConsecutiveOnes(nums))
class Solution(object):
    def singleNumber(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(0, len(nums)):
            result ^= nums[i]
        return result

A = [6, 2, 3, 3, 2, 4, 5, 4, 6]
s = Solution()
print(s.singleNumber(A))
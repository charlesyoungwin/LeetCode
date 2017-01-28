
class Solution(object):
    def singleNumber(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i - 1]:
                return nums[i - 1]
        return -1

A = [6, 2, 3, 3, 2, 4, 5, 4, 6]
s = Solution()
print(s.singleNumber(A))


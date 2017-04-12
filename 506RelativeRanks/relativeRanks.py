class Solution(object):
    def findRelativeRank(self, nums):
        """

        :type nums: List[int]
        :rtype: List[str]
        """

        nums.sort()
        List = ["Gold Medal", "Siver Medal", "Bronze Medal"]
        for i in range(3, len(nums)):
            List.append(str(nums[i]))

input = [5, 4, 3, 2, 1]
solution = Solution(
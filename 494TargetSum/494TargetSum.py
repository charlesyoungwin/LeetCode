class Solution:
    #not ac time exceeded
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        mem = {}

        def helper(index, value):
            if index == len(nums):
                if value == 0:
                    return 1
                else:
                    return 0
            res = mem.get((index, value))
            if res:
                return res
            else:
                mem[(index, value)] =  \
                helper(index + 1, value + nums[index]) \
                + helper(index + 1, value - nums[index])
                return mem[(index, value)]
        return helper(0, S)

    def findTargetSumWaysV2(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        numSum = sum(nums)
        if numSum < S or (S + numSum) % 2 != 0:
            return 0
        else:
            return self.subsetSum(nums, (S + numSum) // 2)

    def subsetSum(self, nums, S):
        dp = [0 for _ in range(0, S + 1)]
        dp[0] = 1
        for n in nums:
            for i in range(S, n - 1, -1):
                dp[i] += dp[i - n]
        return dp[S]

if __name__ == '__main__':
    nums = [1,1,1,1,1]
    solu = Solution()
    print(solu.findTargetSumWaysV2(nums, 3))
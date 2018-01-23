class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        def helper(index, value):
            # if index ==  len(nums):
            #     nonlocal cnt
            #     if value == S:
            #         cnt += 1
            #     return 
            # # if sum(nums) < value:
            # #     return 
            # helper(index + 1, value - nums[index])
            # helper(index + 1, value + nums[index])
            if index == len(nums):
                if value == 0:
                    return 1
                else:
                    return 0
            return helper(index + 1, value + nums[index]) + helper(index + 1, value - nums[index])
            

        cnt = helper(0, S)
        return cnt

if __name__ == "__main__":
    nums = [42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47]
    print(Solution().findTargetSumWays(nums, 38))

     


        
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def twoSum(nums, target, results):
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append([nums[l], nums[r]])
                    l += 1
                    while l < r and (nums[l] == nums[l - 1]):
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        
        def helper(nums, res, ans):
            for i in range(0, len(nums) - 2):
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    twoSum(nums[i+1:], 0 - nums[i], res)
                    if res and len(res) > 0:
                        for item in res:
                            ans.append([nums[i]] + item)
                res = []
        ans = []
        
        helper(sorted(nums), [], ans)
        return ans

if __name__ == '__main__':
    solu = Solution()
    nums = [ -1, 0, 1, 2]
    print(solu.threeSum(nums))
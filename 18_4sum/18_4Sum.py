class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[List[int]]
        """
        res = []
        self.backtrack(sorted(nums), target, 0, 0, res, [])
        return res

    def backtrack(self, nums, target, index, count, res, temp):
        if count > 4:
            return 
        if count == 4 and sum(temp) == target and temp not in res:
            res.append(list(temp))
        for i in range(index, len(nums)):
            temp.append(nums[i])
            self.backtrack(nums, target, i + 1, count + 1, res, temp)
            temp.pop()

    def fourSumV2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[List[int]]
        """
        def findNSum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return 
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                             l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNSum(nums[i+1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNSum(sorted(nums), target, 4, [], results)
        return results

if __name__ == "__main__":
    solu = Solution()
    nums = [0, 0, 0, 0, 0]
    target = 0
    print("Solution1")
    print(solu.fourSum(nums, target))
    print("Solution2")
    print(solu.fourSumV2(nums, target))
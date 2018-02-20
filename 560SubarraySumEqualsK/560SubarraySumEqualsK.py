class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        sumNum = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sumNum += nums[j]
                if sumNum == k:
                    res += 1
            sumNum = 0
        return res

    # solution2 
    def subarraySumV2(self, nums, k):
        sums = {0: 1}
        res = s = 0
        for n in nums:
            s += n
            res += sums.get(s - k, 0)
            sums[s] = sums.get(s, 0) + 1
        return res



if __name__ == '__main__':
     nums = [1, 1, 1]
     print(Solution().subarraySumV2(nums, 2)) 
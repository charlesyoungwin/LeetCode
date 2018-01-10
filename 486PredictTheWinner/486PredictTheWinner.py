class Solution:

    #not ac, wrong answer ? why?
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True
        res1 = 0
        res2 = 0
        length = len(nums)
        length2 = length
        res = []
        while length > 1:
            gainFirst = nums[0]
            lostFirst = max(nums[1], nums[-1])
            gainLast = nums[-1]
            lostLast = max(nums[0], nums[-2])
            if gainFirst - lostFirst - (gainLast - lostLast) >= 0:
                res.append(nums[0])
                del nums[0]
            else:
                res.append(nums[-1])
                del nums[-1]
            length -= 1
        res.extend(nums)
        for i in range(length2):
            if i & 1:
                res2 += res[i]
            else:
                res1 += res[i]
        if res1 >= res2:
            return True
        else:
            return False

    def PredictTheWinnerV2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = {}
        return self.helper(nums, 0, len(nums) - 1, mem) >= 0

    def helper(self, nums, s, e, mem):
        # return nums[s] if s == e else max(nums[e] - self.helper(nums, s, e - 1),
        #                                   nums[s] - self.helper(nums, s + 1, e))
        if (s, e) not in mem:
            mem[(s, e)] = nums[s] if s == e else \
                max(nums[s] - self.helper(nums, s + 1, e, mem), nums[e] - self.helper(nums, s, e - 1, mem))
        return mem[(s, e)]

if __name__ == '__main__':
    nums = [1, 5, 233, 7]
    nums2 = [1, 5, 2]
    print(Solution().PredictTheWinnerV2(nums))
    print(Solution().PredictTheWinnerV2(nums2))

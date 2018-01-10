class Solution:
<<<<<<< HEAD

    #not ac, wrong answer ? why?
=======
>>>>>>> f40a0cf71a8c7b0a2833c63a3adf8cd0784c64ff
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
<<<<<<< HEAD
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
        pass

if __name__ == '__main__':
    nums = [3606449,6,5,9,452429,7,9580316,9857582,8514433,9,6,6614512,753594,5474165,4,2697293,8,7,1]
    print(Solution().PredictTheWinner(nums))
=======
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
    print(Solution().PredictTheWinner(nums))
    print(Solution().PredictTheWinner(nums2))
>>>>>>> f40a0cf71a8c7b0a2833c63a3adf8cd0784c64ff

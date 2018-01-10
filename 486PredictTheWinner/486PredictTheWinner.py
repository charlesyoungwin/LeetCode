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
        pass

if __name__ == '__main__':
    nums = [3606449,6,5,9,452429,7,9580316,9857582,8514433,9,6,6614512,753594,5474165,4,2697293,8,7,1]
    print(Solution().PredictTheWinner(nums))

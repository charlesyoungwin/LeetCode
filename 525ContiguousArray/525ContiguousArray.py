class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        sumToIndex = {}
        sumToIndex[0] = -1
        numSum = 0
        numMax = 0
        for i in range(len(nums)):
            numSum += nums[i]
            if numSum in sumToIndex:
                numMax = max(numMax, i - sumToIndex[numSum])
            else:
                sumToIndex[numSum] = i
        return numMax

    def findMaxLengthV2(self, nums):
        count = 0
        max_length = 0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index
        return max_length

if __name__ == '__main__':
    nums = [1, 1, 1, 0, 1, 0, 1, 1, 1]
    print(Solution().findMaxLength(nums))

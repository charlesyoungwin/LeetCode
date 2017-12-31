

class Solution:
    #暴力解法，肯定不通过，都懒得粘贴上去，做个对比而已
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = float("-inf")
        for i in range(len(nums)):
            for j in range(len(nums)):
                k = nums[i] ^ nums[j]
                if k > maxNum:
                    maxNum = k
        return maxNum

    #ac
    def findMaximumXOR2(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        maxNum, mask = 0, 0
        for i in range(4, -1, -1):
            mask |= (1 << i)
            numSet = set()
            for num  in nums:
                numSet.add(num & mask)
            tmp = maxNum | (1 << i)
            for prefix in numSet:
                if (tmp ^ prefix) in numSet:
                    maxNum = tmp
        return maxNum

if __name__ == '__main__':
    solu = Solution()
    print(solu.findMaximumXOR2([14,11,7,2]))
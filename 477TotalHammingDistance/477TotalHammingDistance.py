class Solution:

    #not AC: time exceeded
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def calHammingDistance(a, b):
            c = a ^ b
            count = 0
            while c:
                count += c & 1
                c = c >> 1
            return count
        if len(nums) == 0 or len(nums) == 1:
            return 0
        sum = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum += calHammingDistance(nums[i], nums[j])
        return sum

    def totalHammingDistance2(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        bits = [[0, 0] for _ in range(32)]
        for x in nums:
            for i in range(32):
                bits[i][x%2] += 1
                x //= 2
        return sum(x * y for x, y in bits)

if __name__ == '__main__':
    solu = Solution()
    nums = [4, 14, 2, 7]
    print(solu.totalHammingDistance2(nums))




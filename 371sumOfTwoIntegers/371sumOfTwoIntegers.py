class Solution(object):

    def getSum(self, a, b):
        """

        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        sum = a ^ b
        carry = (a & b) << 1
        return self.getSum(sum, carry)

s = Solution()
print(s.getSum(12, 5))
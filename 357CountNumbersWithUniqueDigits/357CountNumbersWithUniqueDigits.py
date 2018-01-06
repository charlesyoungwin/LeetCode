class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choice = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1
        for i in range(min(n, 10)):
            product *= choice[i]
            ans += product
        return ans

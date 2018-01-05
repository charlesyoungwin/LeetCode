class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choice = [9] + [i for i in range(9, 0, -1)]
        res, product = 1, 1
        for i in range(min(10, n)):
            product *= choice[i]
            res += product
        return res

if __name__ == '__main__':
    print(Solution().countNumbersWithUniqueDigits(2))

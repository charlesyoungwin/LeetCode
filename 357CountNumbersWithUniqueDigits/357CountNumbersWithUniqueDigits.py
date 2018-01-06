class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
<<<<<<< HEAD
        choice = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1
        for i in range(min(n, 10)):
            product *= choice[i]
            ans += product
        return ans
=======
        choice = [9] + [i for i in range(9, 0, -1)]
        res, product = 1, 1
        for i in range(min(10, n)):
            product *= choice[i]
            res += product
        return res

if __name__ == '__main__':
    print(Solution().countNumbersWithUniqueDigits(2))
>>>>>>> 233345a5d3d02419c01199e18ba67740a6fc61a3

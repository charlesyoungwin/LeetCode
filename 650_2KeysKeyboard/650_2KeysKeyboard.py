class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 2
        res = 0
        while i * i <= n:
            while n % i == 0:
                res += i
                n = n // i
            i += 1
        return res + n

if __name__ == '__main__':
    print(Solution().minSteps(6))
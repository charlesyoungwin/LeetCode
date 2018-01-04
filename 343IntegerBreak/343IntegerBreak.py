

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 3:
            return 2
        if n == 2:
            return 1
        plist = []
        for i  in range(0, n):
            for j  in range(0, n):
                if 2 * i + 3 * j == n:
                    plist.append((i, j))
        res = map(lambda item : (2 ** item[0]) * (3 ** item[1]), plist)

        return max(res)


if __name__ == '__main__':
    print(Solution().integerBreak(7))
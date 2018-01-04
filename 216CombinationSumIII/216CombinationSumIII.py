class Solution:

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        combinations = []



        def helper(k, n, index, path):
            if k < 0 or n < 0:
                return
            if n == 0 and k == 0:
                combinations.append(path)
            for i in range(index, 10):
                helper(k - 1, n - i, i + 1, path + [i])

        helper(k, n, 1, [])
        return combinations


if __name__ == '__main__':
    k, n = 3, 9
    solu = Solution()
    print(solu.combinationSum3(k, n))


class Solution:


    #参考了下别人的代码
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def helper(k, n, index, path):
            if k < 0 or n < 0:
                return
            if n == 0 and k == 0:
                res.append(path)
            for i in range(index, 10):
                helper(k - 1, n - i, i + 1, path+[i])
        helper(k, n, 1, [])
        return res

    def combinationSum3V2(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def helper(path, k, index, n):
            if len(path) > k:
                return
            if len(path) == k and n == 0:
                copy = list(path)
                res.append(copy)
            for i in range(index, 10):
                if n - i >= 0:
                    path.append(i)
                    helper(path, k, i + 1, n - i)
                    path.pop()
        helper([], k , 1, n)
        return res


    #用了好多trick
    """
    for i in [[]]:
        print(i)
    $ []

    for i in []:
        print(i)
    $ None
    """

    def combinationSum3V3(self, k, n):
        """

        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def combs(k, n, cap):
            if not k:
                return [[]] * (not n)
            return [comb + [last]
                        for last in range(1, cap)
                        for comb in combs(k - 1, n - last, last)]

        return combs(k, n, 10)

    def combinationSum3V4(self, k, n):
        """

        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        combs = [[]]
        for _ in range(k):
            combs = [[first] + comb
                        for comb in combs
                        for first in range(1, comb[0] if comb else 10)]
        return [c for c in combs if sum(c) == n]

if __name__ == '__main__':

    print(Solution().combinationSum3V4(2, 3))
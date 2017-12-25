class Solution:

    # greedy solution
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        cur, res = float('-inf'), 0
        for p in sorted(pairs, key = lambda x : x[1]):
            if cur < p[0]:
                cur, res = p[1], res + 1
        return res

    # dynamic solution
    def findLongestChain2(self, pairs):
        """

        :type pairs: List[List[int]]
        :rtype: int
        """
        sPairs = sorted(pairs, key = lambda x : x[0])
        res = [1 for i in range(0, len(pairs))]
        for i in range(0, len(pairs)):
            for j in range(0, i):
                res[i] = max(res[i], res[j] + 1 if sPairs[j][1] < sPairs[i][0] else res[j])
        return res[-1]



if __name__ == '__main__':
    pairs = [[-10,-8],[8,9],[-5,0],[6,10]]
    solu = Solution()
    print(solu.findLongestChain2(pairs))
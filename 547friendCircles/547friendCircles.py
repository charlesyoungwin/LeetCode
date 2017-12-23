
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        rows, cols = len(M), len(M[0])
        stuList = [i for i in range(0, rows)]
        countNum = len(stuList)

        def union(p, q):
            nonlocal countNum
            pInx = find(p)
            qInx = find(q)
            if pInx == qInx:
                return
            for i in range(0, len(stuList)):
                if stuList[i] == pInx:
                    stuList[i] = qInx
            countNum -= 1

        def find(p):
            return stuList[p]

        def isConnected(p, q):
            return find(p) == find(q)

        for i in range(0, rows):
            for j in range(i, cols):
                if M[i][j] == 1:
                    union(i, j)
        return countNum

if __name__ == '__main__':
    solu = Solution()
    M = [[1,1,0],[1,1,1],[0,1,1]]
    print(solu.findCircleNum(M))

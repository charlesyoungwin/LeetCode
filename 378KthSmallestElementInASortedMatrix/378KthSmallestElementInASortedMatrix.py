import heapq


class Solution:

    #虽然AC了，但这个方法没多大意义。。
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return -1
        res = []
        for item in matrix:
            res.extend(item)
        res.sort()
        return res[k - 1]

    def kthSmallestV2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret

    def kthSmallestV3(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(matrix[0][j], 0, j) for j in range(len(matrix[0]))]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if i + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
        return ret


if __name__ == '__main__':
    matrix = [[1, 5, 9], [9, 13, 14], [12, 13, 15]]
    # matrix = [[1, 2], [1, 3]]
    print("solution1")
    print(Solution().kthSmallest(matrix, 8))
    print("solution2")
    print(Solution().kthSmallestV2(matrix, 8))
    print("solution3")
    print(Solution().kthSmallestV3(matrix, 8))
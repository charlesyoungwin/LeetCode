class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        A = bytes(A)
        B = bytes(B)
        maxLength = 0
        for i in range(len(A)):
            for j in range(i, len(A)):
                if A[i:j+1] in B:
                    maxLength = max(maxLength, j - i + 1)
        return maxLength


    def findLengthV2(self, A, B):
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max(max(row) for row in dp)

if __name__ == '__main__':
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    print(Solution().findLengthV2(A, B))

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        commonLen = self.commonDp(word1, word2, len(word1), len(word2))
        return len(word1) + len(word2) - commonLen * 2

    # def commonLength(self, word1, word2, i, j):
    #     if i == 0 or j == 0:
    #         return 0
    #     if word1[i - 1] == word2[j - 1]:
    #         return self.commonLength(word1, word2, i - 1, j - 1) + 1
    #     else:
    #         return max(self.commonLength(word1, word2, i - 1, j), self.commonLength(word1, word2, i, j - 1))

    def commonDp(self, word1, word2, i, j):
        self.res = [[0 for j in range(0, len(word2) + 1)] for i in range(0, len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    self.res[i][j] = self.res[i - 1][j - 1] + 1
                else:
                    self.res[i][j] = max(self.res[i - 1][j], self.res[i][j - 1])
        return self.res[i][j]

if __name__ == '__main__':
    word1 = "eact"
    word2 = "seat"
    print("solution1:")
    print(Solution().minDistance(word1, word2))
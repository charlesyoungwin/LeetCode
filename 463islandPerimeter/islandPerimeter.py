
class Solution(object):
    def islandPerimeter(self, grid):
        """

        :type grid: List[List[int]]
        :rtype: int
        """
        permeter = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0: permeter += 1
                    if i == n - 1 or grid[i + 1][j] == 0: permeter += 1
                    if j == 0 or grid[i][j - 1] == 0: permeter += 1
                    if j == m - 1 or grid[i][j + 1] == 0: permeter += 1
        return permeter

grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
s = Solution()
print(s.islandPerimeter(grid))
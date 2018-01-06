class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        def crossBrickNum(wall, k):
            count = 0
            for item in wall:
                i = 0
                cross = k
                while cross > 0:
                    cross -= item[i]
                if cross < 0:
                    count += 1
            return count
        min = float("inf")
        for i in range(1, sum(wall[0])):
            count = crossBrickNum(wall, i)
            if count < min:
                min = count
        return min

if __name__ == '__main__':
    wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    print(Solution().leastBricks(wall))
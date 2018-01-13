class Solution:

    #ac first solution
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points or len(points) == 0:
            return 0
        points = sorted(points, key = lambda x: (x[0], x[1]))
        terminal = points[0][1]
        res = 1
        for i in range(1, len(points)):
            if terminal < points[i][0]:
                res += 1
                terminal = points[i][1]
            else:
                terminal = min(points[i][1], terminal)
        return res

    #second solution
    def findMinArrowShotsV2(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points or len(points) == 0:
            return 0
        points = sorted(points, key = lambda x : x[1])
        res, end = 0, float('-inf')
        for point in points:
            if point[0] > end:
                res += 1
                end = point[1]
        return res



if __name__ == '__main__':
    input = [[10,16], [2,8], [1,6], [7,12]]
    print(Solution().findMinArrowShotsV2(input))



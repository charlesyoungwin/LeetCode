class Solution:

    #time exceeded, not ac
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if not wall or len(wall) == 0:
            return
        if all([len(wall[i]) == 1 for i in range(0, len(wall))]):
            return len(wall)
        def crossNum(wall, cross):
            count = 0
            for item in wall:
                i = 0
                k = cross
                while k > 0:
                    k -= item[i]
                    i += 1
                if k < 0:
                    count += 1
            return count
        minValue = float("inf")
        for i in range(1, sum(wall[0])):
            count = crossNum(wall, i)
            minValue = min(minValue, count)
        return minValue

    #use dictionary to record the locations and corresponding occurrence
    def leastBricks2(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if not wall or len(wall) == 0:
            return
        res = dict()
        for layer in wall:
            length = 0
            for item in layer[:-1]:
                length += item
                res[length] = res.get(length, 0) + 1
        return len(wall) - max(res.values() if res else [0])

if __name__ == '__main__':
    wall = [[6], [6], [2, 4], [6]]
    print("solution1: ")
    print(Solution().leastBricks(wall))
    print("solution2: ")
    print(Solution().leastBricks2(wall))
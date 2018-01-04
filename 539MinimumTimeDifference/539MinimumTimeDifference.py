class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        res = []
        for item in timePoints:
            res.append(item.split(":"))
        def distance(a, b):
            minuteDiff = abs(a - b)
            return min(minuteDiff, 1440 - minuteDiff)
        minDiff = float("inf")
        minuteList = list(map(lambda item: 60 * int(item[0]) + int(item[1]), res))
        minuteList.sort()
        for i in range(0, len(minuteList) - 1):
            if distance(minuteList[i + 1], minuteList[i]) < minDiff:
                minDiff = distance(minuteList[i + 1], minuteList[i])
        return min(minDiff, distance(minuteList[0], minuteList[-1]))

if __name__ == '__main__':
    timePoints = ["01:01","02:01","03:00"]
    print(Solution().findMinDifference(timePoints))


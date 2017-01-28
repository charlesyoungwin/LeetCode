import math
class Solution(object):
    def constructRectangle(self, area):
        """

        :type area: int
        :rtype: List[int]
        """
        mid = int(math.sqrt(area))
        while mid > 0:
            if area % mid == 0:
                return [int(area / mid), int(mid)]
            mid -= 1


class Solution(object):
    def constructRectangle(self, area):
        """

        :type area: int
        :rtype: List[int]
        """
        min = float('inf')
        for i in range(1, area // 2 + 2):
            t = area % i
            if t == 0:
                m = area // i
                diff = m - i
                if diff >= 0 and diff < min:
                    min = diff
                    t1 = m
                    t2 = i
        return [t1, t2]

s = Solution()
print(s.constructRectangle(1))


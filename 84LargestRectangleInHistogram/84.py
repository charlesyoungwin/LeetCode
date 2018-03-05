class Solution:
    #solution 1
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return self.maxArea(heights, 0, len(heights) - 1)

    def maxArea(self, heights, s, e):
        if s > e:
            return 0
        if s == e:
            return heights[s]
        m = (s + e) // 2
        leftmax = self.maxArea(heights, s, m)
        rightmax = self.maxArea(heights, m + 1, e)
        midmax = self.midmaxArea(heights, s, m, e)
        return max(leftmax, rightmax, midmax)

    def midmaxArea(self, heights, s, m, e):
        area = 0
        i = m
        j = m + 1
        h = min(heights[i], heights[j])
        while i >= s and j <= e:
            h = min(h, heights[i], heights[j])
            area = max(area, h * (j - i + 1))
            if i == s:
                j += 1
            elif j == e:
                i -= 1
            else:
                if heights[i - 1] > heights[j + 1]:
                    i -= 1
                else:
                    j += 1
        return area

    #solution 2
    def largestRectangleAreaV2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans

        


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleAreaV2(heights))
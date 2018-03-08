import math
class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))

if __name__ == '__main__':
    print(Solution().bulbSwitch(5))


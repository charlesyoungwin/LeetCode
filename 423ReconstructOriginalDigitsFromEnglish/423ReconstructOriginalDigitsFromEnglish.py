class Solution:
    # ac solution1
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        count = collections.Counter(s)
        zeroNum = count['z']
        count['e'] -= count['z']
        count['r'] -= count['z']
        count['o'] -= count['z']

        sixNum = count['x']
        count['s'] -= count['x']
        count['i'] -= count['x']

        twoNum = count['w']
        count['t'] -= count['w']
        count['o'] -= count['w']

        eightNum = count['g']
        count['e'] -= count['g']
        count['i'] -= count['g']
        count['h'] -= count['g']
        count['t'] -= count['g']

        threeNum = count['t']

        count['h'] -= count['t']
        count['r'] -= count['t']
        count['e'] -= 2 * count['t']

        sevenNum = count['s']
        count['e'] -= 2 * count['s']
        count['v'] -= count['s']
        count['n'] -= count['s']

        fiveNum = count['v']
        count['f'] -= count['v']
        count['i'] -= count['v']
        count['e'] -= count['v']

        fourNum = count['r']
        count['f'] -= fourNum
        count['o'] -= fourNum
        count['u'] -= fourNum

        oneNum = count['o']
        count['n'] -= oneNum
        count['e'] -= oneNum

        nineNum = count['i']

        res = '0' * zeroNum + '1' * oneNum + '2' * twoNum \
              + '3' * threeNum + '4' * fourNum + '5' * fiveNum \
              + '6' * sixNum + '7' * sevenNum + '8' * eightNum \
              + '9' * nineNum

        return res

    # solution2
    def originalDigitsV2(self, s):
        """
        :type s: str
        :rtype: str
        """

        import collections
        count = collections.Counter(s)
        zeroNum = count['z']
        twoNum = count['w']
        fourNum = count['u']
        sixNum = count['x']
        eightNum = count['g']
        oneNum = count['o'] - twoNum - zeroNum - fourNum
        threeNum = count['h'] - eightNum
        fiveNum = count['f'] - fourNum
        sevenNum = count['s'] - sixNum
        nineNum = count['i'] - sixNum - eightNum - fiveNum
        res = '0' * zeroNum + '1' * oneNum + '2' * twoNum \
              + '3' * threeNum + '4' * fourNum + '5' * fiveNum \
              + '6' * sixNum + '7' * sevenNum + '8' * eightNum \
              + '9' * nineNum
        return res


if __name__ == '__main__':
    s = "owoztneoerfviefuro"
    print(Solution().originalDigitsV2(s))

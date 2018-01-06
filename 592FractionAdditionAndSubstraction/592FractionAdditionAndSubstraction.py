class Solution:

    #ac ..
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        from fractions import Fraction

        res = []
        expreList = expression.split("+")
        for item in expreList:

            if item[0] != '-':
                elemList = item.split('-')
                if len(elemList) == 1:
                    res.append(item)
                else:
                    res.append(elemList[0])
                    for i in range(1, len(elemList)):
                        elemList[i] = '-' + elemList[i]
                        res.append(elemList[i])

            else:
                elemList = item.split('-')
                for i in range(1, len(elemList)):
                    elemList[i] = '-' + elemList[i]
                    res.append(elemList[i])

        sum = Fraction('0/1')
        for item in res:
            sum += Fraction(item)
        ans = str(sum)
        if ans.find('/') == -1:
            ans = ans + "/1"
        return ans

    #无fuck说，gorgeous
    def fractionAdditionV2(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        from fractions import Fraction
        res = sum(map(Fraction, expression.replace("+", " +").replace("-", " -").split()))
        return str(res.numerator) + '/' + str(res.denominator)

if __name__ == '__main__':
    s = "1/2+1/2-8/9+8/9"

    print("solution1:")
    print(Solution().fractionAddition(s))

    print("solution2:")
    print(Solution().fractionAdditionV2(s))
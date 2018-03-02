class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        sign = '-' if numerator * denominator < 0 else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator >= denominator:
            intPart = numerator // denominator
            numerator = numerator % denominator
        else:
            intPart = 0
        
        res = sign + str(intPart)
        if numerator == 0:
            return res
        res += '.'
        dic = {}
        dic[numerator] = len(res)

        while numerator != 0:
            numerator *= 10
            res += str(numerator // denominator)
            numerator %= denominator
            if numerator in dic:
                index = dic[numerator]
                res = res[:index] + "(" + res[index:] + ")"
                break
            else:
                dic[numerator] = len(res)
        return res

if __name__ == '__main__':
    solu = Solution()
    print(solu.fractionToDecimal(1, -999))

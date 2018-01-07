class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = str(num)
        length = len(res)
        def func(length, num):
            if length == num:
                return 1
            else:
                return 0
        ans = ""
        for item in res:
            if item == '0':
                length -= 1
                continue
            elif item <= '3':
                ans += 'M' * int(item) * func(length, 4) + 'C' * int(item) * func(length, 3)\
                        + 'X' * int(item) * func(length, 2) + 'I' * int(item) * func(length, 1)
            elif item == '4':
                ans += 'CD' * func(length, 3)  \
                       + 'XL'* func(length, 2) + 'IV'  * func(length, 1)
            elif item == '5':
                ans +=  'D'  * func(length, 3) \
                        + 'L'  * func(length, 2)  + 'V' * func(length, 1)
            elif item <= '8':
                ans +=  ('D' + 'C' * (int(item) - 5)) * func(length, 3) \
                        + ('L' + 'X' * (int(item) - 5)) * func(length, 2)  \
                        + ('V' + 'I' * (int(item) - 5)) * func(length, 1)
            elif item == '9':
                ans += 'CM'  * func(length, 3) \
                        + 'XC'  * func(length, 2)  + 'IX' * func(length, 1)
            length -= 1
        return ans

    def intToRomanV2(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[(num % 10)]
if __name__ == '__main__':
    print("solution1:")
    print(Solution().intToRoman(1986))
    print("solution2:")
    print(Solution().intToRomanV2(1986))
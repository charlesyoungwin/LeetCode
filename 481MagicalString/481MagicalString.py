class Solution:

    #ac two pointers
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        s1 = "122"
        j = 2
        i = 2
        for _ in range(n):
            if s1[j] == "2":
                if s1[i] == '1':
                    s1 += '2' * 2
                    i += 2
                else:
                    s1 += '1' * 2
                    i += 2
            else:
                if s1[i] == '1':
                    s1 += '2'
                    i += 1
                else:
                    s1 += '1'
                    i += 1
            j += 1
        res = 0
        for i in range(0, n):
            if s1[i] == '1':
                res += 1
        return res

    def magicalStringV2(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [1, 2, 2]
        idx = 2
        while len(s) < n:
            s += s[idx] * [s[-1] ^ 3]
            idx += 1
        return s[:n].count(1)




if __name__ == '__main__':
    print("solution1:")
    print(Solution().magicalString(10000))
    print("solution2:")
    print(Solution().magicalStringV2(10000))
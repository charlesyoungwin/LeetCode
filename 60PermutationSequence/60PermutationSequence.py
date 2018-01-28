class Solution:

    #time exceeded
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = [i for i in range(1, n + 1)]
        self.backtrack(nums, res, [])
        ans = ""
        for item in res[k - 1]:
            ans += str(item)
        return ans

    def backtrack(self, nums, res, temp):
        if len(temp) == len(nums):
            res.append(list(temp))
        for i in range(0, len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.backtrack(nums, res, temp)
            temp.pop()

    #solution2
    def getPermutationV2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = []
        factorial.append(1)
        fact = 1
        for i in range(1, n + 1):
            fact *= i
            factorial.append(fact)

        number = []
        for i in range(1, n + 1):
            number.append(i)
        k -= 1
        res = ""
        for i in range(1, n + 1):
            inx = k // factorial[n - i]
            k -= inx * factorial[n - i]
            res += str(number[inx])
            number.pop(inx)
        return res

if __name__ == '__main__':
    n = 7
    k = 245
    print(Solution().getPermutation(n, k))
    print(Solution().getPermutationV2(n, k))
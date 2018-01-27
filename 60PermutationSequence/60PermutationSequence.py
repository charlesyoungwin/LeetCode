class Solution:
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


if __name__ == '__main__':
    n = 9
    k = 54494
    print(Solution().getPermutation(n, k))


class Solution(object):
    def arrayNestingNotAc(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rSet = set()
        maxLen = 0
        for i in range(len(nums)):

            k = nums[i]
            rSet.add(k)
            count = len(rSet)
            while 1:
                rSet.add(nums[k])
                count += 1
                if count != len(rSet):
                    break
                else:
                    k = nums[k]
            maxLen = max(maxLen, len(rSet))
            rSet.clear()

        return maxLen

    def arrayNestingAc1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, step, n = 0, 0, len(nums)
        seen = [False] * n
        for i in range(n):
            while not seen[i]:
                seen[i] = True
                i, step = nums[i], step + 1
            ans = max(ans, step)
            step = 0
        return ans

if __name__ == '__main__':
    A = [5, 4, 0, 3, 1, 6, 2]
    solu =Solution()
    print(solu.arrayNestingAc1(A))


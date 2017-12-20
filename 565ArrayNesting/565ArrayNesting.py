

class Solution(object):
    def arrayNesting(self, nums):
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

if __name__ == '__main__':
    A = [5, 4, 0, 3, 1, 6, 2]
    solu =Solution()
    print(solu.arrayNesting(A))

class Solution:

    #not ac, time exceeded
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in range(0, len(nums))]
        flag = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res[i] = nums[j]
                    flag = 1
                    break
            if flag == 0:
                for k in range(0, i):
                    if nums[k] > nums[i]:
                        res[i] = nums[k]
                        flag = 1
                        break
            if flag == 0:
                res[i] = -1
            flag = 0
        return res

    def nextGreaterElements2(self, nums):
        """

        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1 for _ in range(0, len(nums))]
        stack = [i for i in range(len(nums) - 1, -1, -1)]
        for i in range(len(nums) - 1, -1, -1):
            while stack:
                index = stack[-1]
                if nums[index] > nums[i]:
                    res[i] = nums[index]
                    break
                else:
                    stack.pop()
            stack.append(i)
        return res




if __name__ == '__main__':
    solu = Solution()
    nums = [1, 4, 2, 3, 5, 2]
    print(solu.nextGreaterElements2(nums))




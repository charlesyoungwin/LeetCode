class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 1, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            cnt = 0
            for elem in nums:
                if elem <= mid:
                    cnt += 1
            if cnt > mid:
                end = mid
            else:
                start = mid + 1

        return start

    def findDuplicateV2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]

            if slow == finder:
                return slow 

if __name__ == '__main__':
    n = 10
    nums = []
    for i in range(1, n + 1):
        nums.append(i)
    nums.append(2)
    print(Solution().findDuplicateV2(nums))

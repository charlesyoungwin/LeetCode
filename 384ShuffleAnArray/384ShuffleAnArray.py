import random

class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        def swap(res, inx1, inx2):
            temp = res[inx1]
            res[inx1] = res[inx2]
            res[inx2] = temp

        res = [item for item in self.nums]
        for i in range(1, len(res)):
            swap(res, i, random.randint(0, i))

        return res



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()
if __name__ == '__main__':
    obj = Solution([1, 3, 5]);
    for _ in range(10):
        print(obj.shuffle())
    print(obj.reset())


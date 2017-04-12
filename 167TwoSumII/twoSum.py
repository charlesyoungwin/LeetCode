class Solution(object):
    def twoSum(self, numbers, target):
        """

        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i

solution = Solution();

#sdsdsd
numbers = [2, 7, 11, 14, 15];
target = 9
print(solution.twoSum(numbers, target))

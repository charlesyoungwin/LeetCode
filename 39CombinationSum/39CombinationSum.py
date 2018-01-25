class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(candidates, target, [], res)
        return res

    def backtrack(self, candidates, target, temp, res):
        if sum(temp) > target:
            return
        if sum(temp) == target:
            tmp = sorted(temp)
            if tmp not in res:
                res.append(list(tmp))

        for i in range(len(candidates)):
            # if candidates[i] in temp:
            #     continue
            temp.append(candidates[i])
            self.backtrack(candidates, target, temp, res)
            temp.pop()

    def combinationSumV2(self, nums, target):
        res = []
        candidates.sort()
        self.backtrackV2(candidates, target, [], res, 0)
        return res

    def backtrackV2(self, candidates, remain, temp, res, start):
        if remain < 0:
            return 
        elif remain == 0:
            res.append(list(temp))
        else:
            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                self.backtrackV2(candidates, remain - candidates[i], temp, res, i)
                temp.pop()

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    print(Solution().combinationSumV2(candidates, 7))
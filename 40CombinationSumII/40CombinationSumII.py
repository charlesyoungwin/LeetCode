class Solution:
    #time exceeded 
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        used = [False for _ in range(len(candidates))]
        self.backtrack(candidates, target, [], res, used)
        return res

    def backtrack(self, candidates, target, temp, res, used):
        if sum(temp) > target:
            return 
        if sum(temp) == target:
            tmp = sorted(temp)
            if tmp not in res:
                res.append(list(tmp))
        for i in range(len(candidates)):
            if used[i]:
                continue
            used[i] = True
            temp.append(candidates[i])
            self.backtrack(candidates, target, temp, res, used)
            used[i] = False
            temp.pop()

    #accepted
    def combinationSum2V2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.backtrackV2(candidates, target, [], res, 0)
        return res

    def backtrackV2(self, candidates, target, temp, res, start):
        if target < 0:
            return 
        if target == 0:
            res.append(list(temp))
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            temp.append(candidates[i])
            self.backtrackV2(candidates, target - candidates[i], temp, res, i + 1)
            temp.pop()

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2V2(candidates, target))
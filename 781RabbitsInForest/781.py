class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0
        res = 0
        dic = {}
        for item in answers:
            dic[item] = dic.get(item, 0) + 1
        for key, value in dic.items():
            if key == 0:
                res += value
            elif key + 1 >= value:
                res += key + 1
            else: 
                res += (value // (key + 1)) * (key + 1)
                if value % (key + 1) != 0:
                    res += key + 1
        return res

    
if __name__ == '__main__':
    answers = [1, 1, 1, 0, 0]
    print(Solution().numRabbits(answers))
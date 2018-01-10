class Solution:
    #no idea, time limit exceeded
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #words = sorted(words, key = lambda x: len(x), reverse = True)
        maxLen = 0
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                flag = 0
                for elem in words[j]:
                    if words[i].find(elem) != -1:
                        flag = 1
                        break
                if flag == 0:
                    length = len(words[i]) * len(words[j])
                    if length > maxLen:
                        maxLen = length
        return maxLen

    def maxProductV2(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key=lambda x: len(x), reverse=True)
        res = []
        alphaList = "abcdefghigklmnopqrstuvwxyz"

        def helper(Origin, divider):

            if divider == 26:
                return

            A = []
            B = []
            for item in Origin:
                if alphaList[divider] in item:
                    A.append(item)
                else:
                    B.append(item)
            if len(A) == 1 or len(B) == 1:
                length = len(A[0]) * len(B[0])
                res.append(length)
            if divider == 25 and len(A) > 1 and len(B) > 1:
                length = len(A[0]) * len(B[0])
                res.append(length)
            helper(A, divider + 1)
            helper(B, divider + 1)
        helper(words, 0)
        return max(res)

if __name__ == '__main__':
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    print(Solution().maxProductV2(words))
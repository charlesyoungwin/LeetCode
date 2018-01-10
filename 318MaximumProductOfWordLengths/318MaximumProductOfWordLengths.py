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
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])


if __name__ == '__main__':
    words = [ 'ababab', 'ab', 'cdcdcd', 'abcd']
    print(Solution().maxProductV2(words))
    print(Solution().maxProduct(words))
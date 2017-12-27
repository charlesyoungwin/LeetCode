class Solution:

    # ac 有点意外。。
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """

        words = sentence.split()
        for i in range(0, len(words)):
            item = words[i]
            length = float("inf")
            for suffix in dict:
                if item.find(suffix, 0, len(suffix)) == -1:
                    continue
                else:
                    if len(suffix) < length:
                        words[i] = suffix
                        length = len(suffix)
        res = ""
        for item in words:
            res += item + " "
        return res[0:-1]

    #ac 大神解法

    def replaceWords2(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dictSet = set(dict)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in dictSet:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))


if __name__ == '__main__':
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    solu = Solution()
    print(solu.replaceWords2(dict, sentence))
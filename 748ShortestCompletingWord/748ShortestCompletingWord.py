class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        import collections
        dicLicense = {}
        for item in licensePlate:
            if str.isalpha(item):
                item = str.lower(item)
                dicLicense[item] = dicLicense.get(item, 0) + 1
        words = sorted(words, key = lambda x: len(x))
        for word in words:
            wordCounter = collections.Counter(str.lower(word))
            flag = 1
            for (k, v) in dicLicense.items():
                if k not in wordCounter or wordCounter[k] < v:
                    flag = 0
            if flag == 1:
                return word

    #version2
    def shortestCompletingWordV2(self, licensePlate, words):
        import collections
        import re
        counter = collections.Counter(re.sub('[^a-z]', '', licensePlate.lower()))
        return min((word for word in words if not counter - collections.Counter(word.lower())), key = len)

if __name__ == '__main__':
    licensePlate = "1s3 456"
    words = ["looks", "pest", "stew", "show"]
    print(Solution().shortestCompletingWordV2(licensePlate, words))
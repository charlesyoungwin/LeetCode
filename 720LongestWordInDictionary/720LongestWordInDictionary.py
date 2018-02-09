class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        wordsSet = set([''])
        longestWord = ''
        for word in words:
            if word[:-1] in wordsSet:
                wordsSet.add(word)
                if len(word) > len(longestWord):
                    longestWord = word
        return longestWord
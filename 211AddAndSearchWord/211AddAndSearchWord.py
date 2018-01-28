class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.wordList = collections.defaultdict(list)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        # if len(self.wordList) == 0:
        #     self.wordList.append(word)
        #     return
        # for i in range(len(self.wordList)):
        #     if i == len(self.wordList) - 1:
        #         self.wordList.append(word)
        #     elif self.wordList[i] > word:
        #         self.wordList.insert(i, word)
        #         break
        if word:
            self.wordList[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if "." not in word:
            return word in self.wordList[len(word)]
        for item in self.wordList[len(word)]:
            success = True
            for index, char in item:
                if char != word[index] and word[index] != '.':
                    success = False
                    break
            if success:
                return True
        return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("aa")
    print(obj.search('bad'))
    print(obj.search("sad"))
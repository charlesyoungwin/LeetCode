class Solution:
    #version 1
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
        cows = both - bulls
        res = str(bulls) + "A" + str(cows) + "B"
        return res

    #version 2
    def getHintV2(self, secret, guess):
        bulls = cows = 0
        sArray = [0 for i in range(10)]
        gArray = [0 for i in range(10)]
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                sArray[int(secret[i])] += 1
                gArray[int(guess[i])] += 1
        cows = sum(min(sArray[i], gArray[i]) for i in range(10))
        res = "%dA%dB" % (bulls, cows)
        return res

if __name__ == '__main__':
    secret = "1807"
    guess = "7801"
    print(Solution().getHint(secret, guess))
    print(Solution().getHintV2(secret, guess))

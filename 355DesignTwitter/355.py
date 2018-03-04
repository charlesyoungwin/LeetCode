class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.follows = {}
        self.cnt = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.dic:
            self.dic[userId] = [(tweetId, self.cnt)]
            self.cnt += 1
        else:
            self.dic[userId].append((tweetId, self.cnt))
            self.cnt += 1
        if userId not in self.follows:
            self.follows[userId] = [userId]

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res = []
        ans = []
        for follower in self.follows.get(userId, []):
            res.extend(self.dic.get(follower, []))
        res = sorted(res, key = lambda x: x[1], reverse = True)
        if len(res) <= 10:
            ans = [res[i][0] for i in range(len(res))]
        else:
            ans = [res[i][0] for i in range(10)]
        return ans


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.follows:
            self.follows[followerId] = [followeeId]
        else:
            if followeeId not in self.follows[followerId]:
                self.follows[followerId].append(followeeId)
        if followerId not in self.follows[followerId]:
            self.follows[followerId].append(followerId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId and followeeId in self.follows.get(followerId, []):
            self.follows[followerId].remove(followeeId)


if __name__ == '__main__':
    obj = Twitter()
    obj.postTweet(1, 5)
    print(obj.getNewsFeed(1))
    obj.follow(1, 2)
    print(obj.getNewsFeed(1))
    obj.postTweet(2, 6)
    print(obj.getNewsFeed(1))
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
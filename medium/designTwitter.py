class Twitter(object):
    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1 # to use for min heap
    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        result = [] # list of tweets 
        heap = []

        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId not in self.tweet_map:
                continue
            i = len(self.tweet_map[followeeId]) -1
            count, tweetId = self.tweet_map[followeeId][i]
            heap.append([count, tweetId, followeeId, i - 1])
        heapq.heapify(heap)

        #i-1 since we add the next index
        while heap and len(result) < 10:
            count, tweetId, followeeId, i = heapq.heappop(heap)
            result.append(tweetId)
            if i >= 0:
                count, tweetId = self.tweet_map[followeeId][i]
                heapq.heappush(heap, [count, tweetId, followeeId, i-1])
        return result
    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follow_map[followerId].add(followeeId)
    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

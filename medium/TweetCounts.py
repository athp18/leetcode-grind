class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.frequencies = {
            'minute': 60,
            'hour': 3600,
            'day': 86400
        }
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.tweets:
            return []
        
        c_size = self.frequencies[freq]
        c_count = (endTime - startTime) // c_size + 1
        res = [0] * c_count

        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                c_index = (time - startTime) // c_size
                res[c_index] += 1
        
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

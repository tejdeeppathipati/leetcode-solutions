class Twitter:

    def __init__(self):
        self.count = 0
        self.userMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        minHeap = []

        self.userMap[userId].add(userId)
        for followeeId in self.userMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append((count, tweetId, followeeId, index))

        heapq.heapify(minHeap)
        while minHeap and len(feed) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            feed.append(tweetId)
            index -= 1

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index))
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userMap[followerId]:
            self.userMap[followerId].remove(followeeId)

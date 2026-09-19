class Twitter:

    def __init__(self):
        self.posts = dict()
        self.follows = dict()
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append([-self.timestamp, tweetId])
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        maxHeap = []
        if userId in self.posts:
            maxHeap.extend(self.posts[userId])
        if userId in self.follows:
            for user in self.follows[userId]:
                if user in self.posts:
                    maxHeap.extend(self.posts[user])
        heapq.heapify(maxHeap)

        while maxHeap and len(result) < 10:
            result.append(heapq.heappop(maxHeap)[1])
        return result

        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = []
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()  # stores [-remaining_count, ready_time]

        while maxHeap or q:
            time += 1
            if maxHeap:
                popped = heapq.heappop(maxHeap)
                if popped + 1 < 0:
                    q.append([popped + 1, time + n])
            while q and q[0][1] <= time:
                heapq.heappush(maxHeap, q[0][0])
                q.popleft()
        return time
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heapCount = {}
        maxHeap = []
        queue = []
        time = 0

        for task in tasks:
            if task not in heapCount:
                heapCount[task] = 0
            heapCount[task] += 1
        for char in heapCount:
            heapq.heappush(maxHeap, [-heapCount[char], char])

        while len(maxHeap) > 0 or len(queue) > 0:
            if len(maxHeap) == 0:
                time = queue[0][0]
            else:
                popped = heapq.heappop(maxHeap)
                time += 1
                popped[0] += 1
                if popped[0] != 0:
                    queue.append([time + n, popped])
            
            if len(queue) > 0 and queue[0][0] == time:
                item = queue.pop(0)
                heapq.heappush(maxHeap, item[1])
        return time
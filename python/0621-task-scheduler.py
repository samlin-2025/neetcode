class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = Counter(tasks)
        maxHeap = [-v for v in hashmap.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while q or maxHeap:
            time += 1;
            if maxHeap:
                cnt = -heapq.heappop(maxHeap) - 1
                if cnt > 0:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, -q[0][0]) #always do a heappusgh
                q.popleft()
            
        return time
                

# Greedy algorithm
class Solution(object):
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_count = max(counter.values())
        min_time = (max_count - 1) * (n + 1) + \
                    sum(map(lambda count: count == max_count, counter.values()))
    
        return max(min_time, len(tasks))
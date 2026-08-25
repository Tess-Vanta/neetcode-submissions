"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key= lambda x: x.start)
        pq = []
        heapq.heappush(pq, intervals[0].end)

        for i in range(1, len(intervals)):
            curr = intervals[i]

            if curr.start >= pq[0]:
                heapq.heappop(pq)
            
            heapq.heappush(pq, curr.end)
        
        return len(pq)
            
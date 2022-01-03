from heapq import *

class MedianFinder(object):  # Runtime: 740 ms, faster than 85.37%
    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def addNum(self, num):  # O(log n)
        if len(self.min_heap) + len(self.max_heap) == 0:
            heappush(self.min_heap, num)
        else:
            if num >= self.min_heap[0]:
                heappush(self.min_heap, num)  # insert into min heap
                if len(self.min_heap) - len(self.max_heap) > 1:
                    heappush(self.max_heap, -heappop(self.min_heap))
            else:
                heappush(self.max_heap, -num)  # insert into max heap
                if len(self.max_heap) > len(self.min_heap):
                    heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self):  # O(1)
        if len(self.min_heap) + len(self.max_heap) > 0:
            if (len(self.min_heap) + len(self.max_heap)) % 2 != 0:
                return float(self.min_heap[0])
            else:
                return (-self.max_heap[0] + self.min_heap[0]) / 2.0


# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print obj.findMedian()
# obj.addNum(3)
# print obj.findMedian()

obj = MedianFinder()
obj.addNum(5)
obj.addNum(6)
obj.addNum(2)
obj.addNum(1)
obj.addNum(8)
obj.addNum(5)
obj.addNum(4)
obj.addNum(3)
obj.addNum(12)
obj.addNum(10)
print obj.findMedian()
obj.addNum(7)
print obj.findMedian()
print obj.findMedian()

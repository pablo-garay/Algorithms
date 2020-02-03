import heapq

class Solution(object):  # Time complexity: O(n) + O(K log n)
    def kClosest(self, points, K):
        mapping = {}  # 25 -> [(0, 5), (5, 0)]    9 -> [(0, 3), (3, 0)]

        li_distances = []
        for (x, y) in points:  # iterate each point in list  # O(n)
            distance = x ** 2 + y ** 2

            if distance not in mapping:
                mapping[distance] = []

            mapping[distance].append([x, y])
            li_distances.append(distance)

        heapq.heapify(li_distances)  # O(n)

        result = []
        for i in xrange(K):  # O(K log n)
            next_min_distance = heapq.heappop(li_distances)  # O(log n)
            coords = mapping[next_min_distance].pop()

            result.append(coords)

        return result


print Solution().kClosest(points = [[1,3],[-2,2]], K = 1)
print Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2)
print Solution().kClosest(points = [[-10000, -10000]], K = 1)
print Solution().kClosest(points = [[10000, 10000]], K = 1)
